from ewoksorange.tests.utils import execute_task
from ewoksxrpd.tasks.sum import SumBlissScanImages, SumImages
import pytest
import os.path


@pytest.mark.parametrize("monitor_name", ("mon", None))
@pytest.mark.parametrize("skip_dark", [False, True])
def test_sum_bliss_scan(tmpdir, bliss_perkinelmer_scan, monitor_name, skip_dark):
    inputs = {
        "filename": str(bliss_perkinelmer_scan),
        "detector_name": "perkinelmer",
        "output_filename": str(tmpdir / "output.h5"),
        "scan": 2,
        "monitor_name": monitor_name,
        "skip_dark": skip_dark,
    }

    outputs = execute_task(
        SumBlissScanImages,
        inputs=inputs,
    )

    assert os.path.isfile(str(tmpdir / "output.h5"))
    assert isinstance(outputs["output_uri"], str)


@pytest.mark.parametrize("monitor_name", ("mon", None))
def test_sum(tmpdir, bliss_perkinelmer_scan, monitor_name):
    inputs = {
        "filename": str(bliss_perkinelmer_scan),
        "detector_name": "perkinelmer",
        "output_filename": str(tmpdir / "output.h5"),
        "start_scan": 2,
        "end_image": 10,
        "end_scan": 2,
        "monitor_name": monitor_name,
    }

    outputs = execute_task(
        SumImages,
        inputs=inputs,
    )

    assert os.path.isfile(str(tmpdir / "output.h5"))
    assert len(outputs["output_uris"]) == 1


def test_sum_type_both(tmpdir, bliss_perkinelmer_scan):
    inputs = {
        "filename": str(bliss_perkinelmer_scan),
        "detector_name": "perkinelmer",
        "output_filename": str(tmpdir / "output.h5"),
        "start_scan": 2,
        "end_scan": 2,
        "sum_type": "both",
    }

    outputs = execute_task(
        SumImages,
        inputs=inputs,
    )

    assert os.path.isfile(str(tmpdir / "output.h5"))
    # Scan sum and full sum
    assert len(outputs["output_uris"]) == 2
