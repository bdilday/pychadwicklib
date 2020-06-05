"""script to update c source-code files with notice of modification for GPL-2 license"""

import datetime
import glob
import logging

logging.basicConfig(level=logging.INFO)


def update_text(text):
    boilerplate = (
        "/* This source code was modified by Ben Dilday on {}\n"
        " * for inclusion on the pychadwicklib project\n"
        " * https://github.com/bdilday/pychadwicklib\n"
        " * The original is available at https://github.com/chadwickbureau/chadwick\n"
        "*/\n".format(timestamp)
    )
    return boilerplate + text


def update_file(file_path):
    updated_file_path = file_path
    logging.info(f"writing file {file_path} to {updated_file_path}")
    with open(file_path, "r") as fp:
        existing_text = fp.read()
    with open(updated_file_path, "w") as fp:
        fp.write(update_text(existing_text))


def main():
    files = glob.glob("src/cw*/*.[ch]")
    for file_path in files:
        update_file(file_path)


if __name__ == "__main__":
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    main()
