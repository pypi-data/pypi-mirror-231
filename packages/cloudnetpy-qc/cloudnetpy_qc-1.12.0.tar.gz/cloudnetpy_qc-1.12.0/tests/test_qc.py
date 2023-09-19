"""cloudnetpy-qc tests."""
from os import path
from pathlib import Path

from cloudnetpy_qc import quality

SCRIPT_PATH = path.dirname(path.realpath(__file__))


def test_valid_file():
    # TODO: update this file
    filename = f"{SCRIPT_PATH}/data/20211129_juelich_hatpro.nc"
    check = Check(filename)
    check.errors()
    for test in check.tests:
        exps = test["exceptions"]
        assert (
            exps
            if test["testId"]
            in ("TestInstrumentPid", "TestUnits", "FindVariableOutliers")
            else not exps
        ), f"{test}, {exps}"


def test_legacy_file():
    filename = f"{SCRIPT_PATH}/data/20120203_arm-maldives_classification.nc"
    check = Check(filename, file_type="classification")
    keys = [
        "TestLongNames",
        "TestStandardNames",
        "TestDataTypes",
        "TestGlobalAttributes",
        "TestVariableNames",
        "TestCFConvention",
    ]
    check.verify_exceptions(keys)


def test_missing_data():
    filename = f"{SCRIPT_PATH}/data/20220729_norunda_cl51.nc"
    check = Check(filename)
    check.verify_exceptions(["TestDataCoverage"])


def test_invalid_lwp():
    filename = f"{SCRIPT_PATH}/data/20220214_schneefernerhaus_hatpro.nc"
    check = Check(filename)
    check.verify_exceptions(["FindVariableOutliers"])


def test_file_without_time_array():
    filename = f"{SCRIPT_PATH}/data/20200505_chilbolton_mira.nc"
    check = Check(filename)
    check.verify_exceptions(["TestTimeVector"])


def test_bad_mwr_from_delft():
    filename = f"{SCRIPT_PATH}/data/20210421_delft_hatpro.nc"
    check = Check(filename)
    check.verify_exceptions(["TestTimeVector"])


def test_bad_mwr_from_granada():
    filename = f"{SCRIPT_PATH}/data/20160610_granada_hatpro.nc"
    check = Check(filename)
    check.verify_exceptions(["TestTimeVector"])


def test_bad_categorize_from_chilbolton():
    filename = f"{SCRIPT_PATH}/data/20001017_chilbolton_categorize.nc"
    check = Check(filename, file_type="categorize")
    check.verify_exceptions(["FindFolding"])


def test_empty_instrument_pid():
    filename = f"{SCRIPT_PATH}/data/20220326_schneefernerhaus_mira.nc"
    check = Check(filename)
    check.verify_exceptions(["TestInstrumentPid"])


class Check:
    """Check class."""

    def __init__(self, filename: str, file_type: str | None = None):
        self.report = quality.run_tests(Path(filename), cloudnet_file_type=file_type)
        self.tests = self.report["tests"]

    def verify_exceptions(self, keys: list):
        n = 0
        for test in self.tests:
            if test["testId"] in keys:
                assert test["exceptions"]
                n += 1
        assert n == len(keys)

    def errors(self, n_expected: int = 0):
        assert self._count("error") == n_expected

    def warnings(self, n_expected: int = 0):
        assert self._count("warning") == n_expected

    def _count(self, level: str):
        n = 0
        for test in self.report["tests"]:
            for exp in test["exceptions"]:
                if exp["result"] == level:
                    n += 1
        return n
