import gzip
import zipfile
import pathlib
def decompress_file(archive_path, output_dir):
    archive_type = pathlib.Path(archive_path).suffix
if __name__ == "__main__":
    archive_path = input("Source archive file: ")
    output_dir = input("Output directory: ")
    decompress_file(archive_path, output_dir)
