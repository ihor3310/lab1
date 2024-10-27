import gzip
import zipfile
import pathlib
def decompress_file(archive_path, output_dir):
    archive_type = pathlib.Path(archive_path).suffix
