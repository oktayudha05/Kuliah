import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkAmber')

fileExcel = 'biodata.xlsx'

isiExcel = pd.read_excel(fileExcel)

form = [
    [sg.Text('Nama'), sg.InputText(key='nama')],
    [sg.Text('NPM'), sg.InputText(key='npm')],
    [sg.Text('Jenis Kelamin'), sg.Combo(['Laki-laki', 'Perempuan'], key='jenis_kelamin')],
    [sg.Text('Jurusan'), sg.InputText(key='jurusan')],
    [sg.Text('Alamat'), sg.Multiline(key='alamat')],
    [sg.Text('Email'), sg.InputText(key='email')],
    [sg.Text('Moto'), sg.InputText(key='moto')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()],
]

window = sg.Window('Tugas Akhir', form)


def hapusInput():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Clear':
        hapusInput()
    elif event == 'Submit':
        isiExcel = isiExcel._append(values, ignore_index=True)
        isiExcel.to_excel(fileExcel, index=False)
        hapusInput()
        sg.popup('Data berhasil disimpan')
        
window.close()