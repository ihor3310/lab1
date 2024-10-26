import datetime
import zipfile
import gzip
import pathlib

def cmprs_f(filename, out_dir, archive_type="gz"):
    archive_name = generate_archive_name(filename)
    output_path = pathlib.Path(out_dir) / f"{archive_name}.{archive_type}"

if __name__ == "__main__":
    source_f = input("Source file: ")
    output_d = input("Output directory: ")
    archive_t = input("Archive type (gz/zip): ")
    cmprs_f(source_f, output_d, archive_t)
