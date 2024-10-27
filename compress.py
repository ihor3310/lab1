import datetime
import zipfile
import gzip
import pathlib

def gen_arch_name(filename):
    date = datetime.datetime.now().strftime("%Y%m%d")
    archive_number = 1
    base_n = pathlib.Path(filename).stem
    archive_name = f"{base_n}_{date}_{archive_number}"
    return archive_name

def cmprs_f(filename, out_dir, archive_type="gz"):
    archive_name = gen_arch_name(filename)
    output_path = pathlib.Path(out_dir) / f"{archive_name}.{archive_type}"
    if archive_type == "gz":
        with open(filename, "rb") as f_in, gzip.open(output_path, "wb") as f_out:
            while True:
                data = f_in.read(1024)
                if not data:
                    break
                f_out.write(data)
    elif archive_type == "zip":
        with zipfile.ZipFile(output_path, "w") as archive:
            archive.write(filename, arcname=pathlib.Path(filename).name)
    print(f"File compressed as: {output_path}")

if __name__ == "__main__":
    source_f = input("Source file: ")
    output_d = input("Output directory: ")
    archive_t = input("Archive type (gz/zip): ")
    cmprs_f(source_f, output_d, archive_t)
