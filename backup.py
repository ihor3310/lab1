import os
import tarfile
import datetime
import pathlib
import argparse

def create_bckp(source_dir, extensions, output_dir, archive_type):
    files_to_backup = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.split('.')[-1] in extensions:
                file_path = pathlib.Path(root) / file
                files_to_backup.append(file_path)
    date = datetime.datetime.now().strftime("%Y%m%d")
    archive_name = f"{pathlib.Path(source_dir).name}_{date}_{len(list(pathlib.Path(output_dir).glob(f'*_{date}_*.tar.{archive_type}'))) + 1}.tar.{archive_type}"

    with tarfile.open(pathlib.Path(output_dir) / archive_name, f"w:{archive_type}") as archive:
        for file_path in files_to_backup:
            archive.add(file_path, arcname=file_path.relative_to(source_dir))
    print(f"Archive created: {archive_name}")
def restore_backup(archive_path, output_dir):
    with tarfile.open(archive_path, "r:*") as archive:
        archive.extractall(output_dir)
    print(f"Archive restored to {output_dir}")    
if __name__ == "__main__":
    prsr = argparse.ArgumentParser(description="Backup or restore files.")
    prsr.add_argument("operation", choices=["c", "d"], help="Operation: 'c' to compress or 'd' to decompress.")
    args = prsr.parse_args()
    
