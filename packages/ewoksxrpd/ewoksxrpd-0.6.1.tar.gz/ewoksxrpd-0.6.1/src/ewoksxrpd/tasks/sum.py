from typing import Optional
from ewokscore import Task
from blissdata.h5api import dynamic_hdf5
import h5py

from ewoksxrpd.tasks.data_access import TaskWithDataAccess

from .utils.sum_utils import ImageSum, generate_range, save_sum

SUM_TYPES = ["per_scan", "all_scans", "both"]


class SumBlissScanImages(
    TaskWithDataAccess,
    input_names=["filename", "scan", "detector_name", "output_filename"],
    optional_input_names=[
        "monitor_name",
        "subscan",
        "scan_memory_url",
        "output_process",
        "skip_dark",
    ],
    output_names=["output_uri"],
):
    """Sum images of a single camera of a single Bliss scan"""

    def run(self):
        filename: str = self.inputs.filename
        scan: int = self.inputs.scan
        subscan = self.get_input_value("subscan", 1)
        detector_name: str = self.inputs.detector_name
        output_filename: str = self.inputs.output_filename
        output_url = f"silx://{output_filename}?path=/{scan}.{subscan}"
        monitor_name: Optional[str] = self.get_input_value("monitor_name", None)
        output_process: str = self.get_input_value("output_process", "sum")
        skip_dark: bool = self.get_input_value("skip_dark", False)

        if monitor_name:
            counter_names = [monitor_name]
        else:
            counter_names = None

        if self.inputs.scan_memory_url:
            data_iterator = self.iter_bliss_data_from_memory(
                self.inputs.scan_memory_url,
                lima_names=[detector_name],
                counter_names=counter_names,
            )

            # Dark images are even indices when in memory
            def is_dark(image_number):
                return image_number % 2 == 0

        else:
            data_iterator = self.iter_bliss_data(
                filename,
                scan,
                lima_names=[detector_name],
                counter_names=counter_names,
                subscan=subscan,
            )
            with dynamic_hdf5.File(
                filename, lima_names=[detector_name], **self.get_retry_options()
            ) as root:
                dataset_shape = root[
                    f"{scan}.{subscan}/instrument/{detector_name}/data"
                ].shape
                nb_points_in_scan = dataset_shape[0]

            # Dark images are put at the end once the scan is saved
            def is_dark(image_number):
                return image_number >= nb_points_in_scan // 2

        with self.open_h5item(output_url, mode="a", create=True) as output:
            sum_process = output.create_group(output_process)
            sum_process.attrs["NX_class"] = "NXprocess"
            sum_process.attrs["default"] = "results"
            nxdata = sum_process.create_group("results")
            nxdata.attrs["NX_class"] = "NXdata"

            scan_sum = None
            summed_indices = []
            for image_number, ptdata in enumerate(data_iterator):
                if skip_dark and is_dark(image_number):
                    continue

                image = ptdata[detector_name]
                if scan_sum is None:
                    scan_sum = ImageSum(image.shape)

                if monitor_name is not None:
                    monitor = ptdata[monitor_name]
                else:
                    monitor = None

                scan_sum.add_to_sum(image, monitor)
                summed_indices.append(image_number)

            if scan_sum:
                dset = save_sum(
                    nxdata,
                    name=f"Scan{scan}-Images{summed_indices[0]}-{summed_indices[-1]}",
                    image_sum=scan_sum,
                )

                self.outputs.output_uri = f"{nxdata.file.filename}::{dset.name}"


class SumImages(
    Task,
    input_names=["filename", "detector_name", "output_filename"],
    optional_input_names=[
        "start_scan",
        "end_scan",
        "start_image",
        "end_image",
        "block_size",
        "monitor_name",
        "output_entry",
        "output_process",
        "sum_type",
    ],
    output_names=["output_uris"],
):
    """Sum images of a single camera from a Bliss scan file

    For each scan, images are added in blocks of `block_size` images (one block with all images by default).

    The result contains:
        * the block sums when sum_type=per_scan or sum_type=both
        * the sum of the block sums when sum_type=all_scans or sum_type=both
    """

    def run(self):
        filename: str = self.inputs.filename
        detector_name: str = self.inputs.detector_name
        output_filename: str = self.inputs.output_filename
        start_scan: int = self.get_input_value("start_scan", 1)
        end_scan: Optional[int] = self.get_input_value("end_scan", None)
        start_image: int = self.get_input_value("start_image", 0)
        end_image: Optional[int] = self.get_input_value("end_image", None)
        block_size: Optional[int] = self.get_input_value("block_size", None)
        monitor_name: Optional[str] = self.get_input_value("monitor_name", None)
        output_entry: str = self.get_input_value("output_entry", "processing")
        output_process: str = self.get_input_value("output_process", "sum")
        sum_type: str = self.get_input_value("sum_type", "per_scan")

        if sum_type not in SUM_TYPES:
            raise TypeError(
                f"sum_type must be one of the following values: {SUM_TYPES}. Got {sum_type} instead."
            )
        save_scan_sums = sum_type == "per_scan" or sum_type == "both"
        save_full_sum = sum_type == "all_scans" or sum_type == "both"

        with h5py.File(filename, "r") as h5file:
            nscans = len(h5file)
            scan_range = generate_range(start_scan, end_scan, nscans + 1)

            first_scan_name = list(h5file.keys())[0]
            nimages, *detector_shape = h5file[
                f"{first_scan_name}/measurement/{detector_name}"
            ].shape
            image_range = list(generate_range(start_image, end_image, nimages))

            scan_sum = ImageSum(detector_shape)
            full_sum = ImageSum(detector_shape)

            with h5py.File(output_filename, "a") as output:
                entry = output.require_group(output_entry)
                entry.attrs["NX_class"] = "NXentry"
                entry.attrs["default"] = output_process
                sum_process = entry.create_group(output_process)
                sum_process.attrs["NX_class"] = "NXprocess"
                sum_process.attrs["default"] = "results"
                results = sum_process.create_group("results")
                results.attrs["NX_class"] = "NXdata"

                output_uris = []
                for scan_number in scan_range:
                    scan_images = h5file[f"{scan_number}.1/measurement/{detector_name}"]
                    monitor_data = (
                        h5file[f"{scan_number}.1/measurement/{monitor_name}"]
                        if monitor_name
                        else None
                    )
                    assert isinstance(scan_images, h5py.Dataset)
                    if monitor_data is not None:
                        assert isinstance(monitor_data, h5py.Dataset)

                    for image_number in image_range:
                        image = scan_images[image_number]
                        monitor = monitor_data[image_number] if monitor_data else None
                        scan_sum.add_to_sum(image, monitor)
                        full_sum.add_to_sum(image, monitor)

                        if save_scan_sums and scan_sum.nb_images == block_size:
                            dset = save_sum(
                                results,
                                name=f"Scan{scan_number}-Images{image_number - scan_sum.nb_images + 1}-{image_number}",
                                image_sum=scan_sum,
                            )
                            output_uris.append(f"{output_filename}::{dset.name}")

                            # Move to next sum
                            scan_sum.reset()

                    if save_scan_sums and scan_sum.nb_images > 0:
                        dset = save_sum(
                            results,
                            name=f"Scan{scan_number}-Images{image_number - scan_sum.nb_images + 1}-{image_number}",
                            image_sum=scan_sum,
                        )
                        output_uris.append(f"{output_filename}::{dset.name}")
                        # Move to next sum
                        scan_sum.reset()

                if save_full_sum:
                    dset = save_sum(
                        results,
                        name=f"Sum of scans {scan_range.start} to {scan_range.stop - scan_range.step}",
                        image_sum=full_sum,
                    )
                    output_uris.append(f"{output_filename}::{dset.name}")

        self.outputs.output_uris = output_uris
