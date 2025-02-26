import pytest
from utilities.file_utils import check_file_exists

@pytest.mark.parametrize("file_path", [
    "C:\\GRL\\GRL-C3-MP-TPT\\Readme.txt",
    "C:\\GRL\\GRL-C3-MP-TPT\\GRL-C3-TPT Release Notes.pdf",
    "C:\\GRL\\GRL-C3-MP-TPT\\Firmware_Files\\BPP_EPP\\PPS_ELOAD.bin",
    "C:\\GRL\\GRL-C3-MP-TPT\\Firmware_Files\\BPP_EPP\\BOOT.bin"
])
def test_check_files(file_path):
    """
    Test to check if the files exist at the specified paths.
    """
    assert check_file_exists(file_path), f"File {file_path} does not exist"

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])