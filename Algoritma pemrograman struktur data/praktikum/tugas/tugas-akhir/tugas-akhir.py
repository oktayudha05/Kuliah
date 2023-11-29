import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkAmber')

fileXlsx = 'biodata.xlsx'

df = pd.read_excel(fileXlsx)

layout = [
    [sg.Text('Nama'), sg.InputText(key='nama')],
    [sg.Text('NPM'), sg.InputText(key='npm')],
    [sg.Text('Jenis Kelamin'), sg.Combo(['Laki-laki', 'Perempuan'], key='jenis_kelamin')],
    [sg.Text('Jurusan'), sg.InputText(key='jurusan')],
    [sg.Text('Alamat'), sg.Multiline(key='alamat')],
    [sg.Text('Email'), sg.InputText(key='email')],
    [sg.Text('Moto'), sg.InputText(key='moto')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()],
]

window = sg.Window('Tugas Akhir', layout)


def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Clear':
        clear_input()
    elif event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(fileXlsx, index=False)
        clear_input()
        sg.popup('Data berhasil disimpan')
window.close()