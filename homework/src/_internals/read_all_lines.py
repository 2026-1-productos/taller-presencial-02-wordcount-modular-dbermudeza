import os


def read_all_lines(input_folder):
    """Read all lines from all files in the input folder."""
    lines = []
    for entry in sorted(os.scandir(input_folder), key=lambda entry: entry.name):
        if not entry.is_file():
            continue
        with open(entry.path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines
