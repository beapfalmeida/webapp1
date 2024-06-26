import zipfile
import pathlib

def make_archive(filepaths, dest_folder):
    destiny = pathlib.Path(dest_folder, "compressed.zip")
    with zipfile.ZipFile(destiny, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name) # ??? não percebi super bem estas duas linhas