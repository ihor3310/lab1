import datetime
import zipfile
import gzip
import pathlib



if __name__ == "__main__":
    source_f = input("Source file: ")
    output_d = input("Output directory: ")
    archive_t = input("Archive type (gz/zip): ")
    compress_file(source_f, output_d, archive_t)
