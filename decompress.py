import gzip
import zipfile
import pathlib
def decompress_file(archive_path, output_dir):
    archive_type = pathlib.Path(archive_path).suffix
    if archive_type == ".gz":
        output_path = pathlib.Path(output_dir) / pathlib.Path(archive_path).stem
        with gzip.open(archive_path, "rb") as f_in, open(output_path, "wb") as f_out:
            while True:
                data = f_in.read(1024)
                if not data:
                    break
                f_out.write(data)
    elif archive_type == ".zip":
        with zipfile.ZipFile(archive_path, "r") as archive:
            archive.extractall(output_dir)

    print(f"Archive decompressed to: {output_dir}")

if __name__ == "__main__":
    archive_path = input("Source archive file: ")
    output_dir = input("Output directory: ")
    decompress_file(archive_path, output_dir)

