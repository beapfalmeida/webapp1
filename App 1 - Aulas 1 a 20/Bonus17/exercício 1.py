import PySimpleGUI as SG
lable1 = SG.Text("Enter feet: ")
input_box1 = SG.InputText(key="feet")

lable2 = SG.Text("Enter inches: ")
input_box2 = SG.InputText(key="inches")

convert_button = SG.Button("Convert")
result_lable = SG.Text(key='result', text_color='white')

window = SG.Window("Convertor", layout=[[lable1,input_box1],[lable2, input_box2],
                                        [convert_button,result_lable]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])
    meters = feet * 0.3048 + inches * 0.0254
    window['result'].update(value=f"{meters} m")

window.close()