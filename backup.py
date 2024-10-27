import os
import tarfile
import datetime
import pathlib
import argparse

if __name__ == "__main__":
    prsr = argparse.ArgumentParser(description="Backup or restore files.")
    prsr.add_argument("operation", choices=["c", "d"], help="Operation: 'c' to compress or 'd' to decompress.")
    args = prsr.parse_args()
