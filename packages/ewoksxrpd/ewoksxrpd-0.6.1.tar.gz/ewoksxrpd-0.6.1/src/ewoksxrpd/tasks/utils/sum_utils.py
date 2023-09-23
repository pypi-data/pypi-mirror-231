from typing import Optional
import h5py
import numpy


class ImageSum:
    def __init__(self, shape) -> None:
        self.shape = shape
        self.summed_image = numpy.zeros(shape)
        self.summed_monitor = 0
        self.nb_images = 0

    def add_to_sum(self, image: numpy.ndarray, monitor: Optional[int]):
        self.summed_image += image
        if monitor is not None:
            self.summed_monitor += monitor
        self.nb_images += 1

    def reset(self):
        self.summed_image = numpy.zeros(self.shape)
        self.summed_monitor = 0
        self.nb_images = 0


def generate_range(start: int, end_arg: Optional[int], nitems: int) -> range:
    end = nitems if end_arg is None else end_arg + 1

    if (end - start) > nitems:
        raise ValueError(
            f"Asked range ({start},{end}) is bigger than number of items ({nitems})"
        )

    return range(start, end)


def save_sum(nxdata: h5py.Group, name: str, image_sum: ImageSum):
    dset = nxdata.create_dataset(name, data=image_sum.summed_image)
    dset.attrs["monitor"] = image_sum.summed_monitor
    dset.attrs["nb_images"] = image_sum.nb_images

    if "signal" not in nxdata:
        nxdata.attrs["signal"] = name

    return dset
