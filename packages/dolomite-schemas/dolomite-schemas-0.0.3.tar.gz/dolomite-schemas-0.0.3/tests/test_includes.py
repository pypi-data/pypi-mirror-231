import os

from dolomite.schemas import get_schema_directory

__author__ = "Jayaram Kancherla"
__copyright__ = "jkanche"
__license__ = "MIT"


def test_includes():
    out = get_schema_directory()
    assert isinstance(out, str)
    assert os.path.isdir(os.path.join(out, "array"))
    assert os.path.isdir(os.path.join(out, "vcf_file"))
    assert os.path.isdir(os.path.join(out, "single_cell_experiment"))
