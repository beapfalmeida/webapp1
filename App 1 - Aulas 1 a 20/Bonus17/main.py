import PySimpleGUI as SG
from zip_creator import make_archive

lable1 = SG.Text("Select files to compress: ")
input1 = SG.Input(key="input_files")
choose_button1 = SG.FilesBrowse("Choose", key="files")

label2 = SG.Text("Select destination folder: ")
input2 = SG.Input(key="input_folder")
choose_button2 = SG.FolderBrowse("Choose",key="folder")

compress_button = SG.Button("Compress")
complete_lable = SG.Text(key="complete")

window = SG.Window("File Compressor", layout=[[lable1, input1, choose_button1], [label2, input2, choose_button2],
                                              [compress_button, complete_lable]])
while True:
    event, values = window.read()
    print(event, values)
    files = values['files'].split(";")
    folder = values['folder']
    if event == 'Compress':
        make_archive(files, folder)
        window['complete'].update(value="Compression completed!")

window.close()

