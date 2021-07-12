from main import main
import PySimpleGUI as sg

def main_gui():

    sg.theme('DarkAmber')

    layout = [  [sg.Text("Qual o id da filial?", justification='left', size=(50,1))],
                [sg.Input(size=(50,1))],
                [sg.Text("Qual o número do broker?", justification='left', size=(50,1))],
                [sg.Input(size=(50,3))],
                [sg.Text("Qual o token de acesso?",justification='left', size=(50,1)),],
                [sg.Input(size=(50,1))],
                [sg.Text("Choose a file: "), sg.FileBrowse()],
                [sg.Button('Iniciar', 'center', size=(42,2))], 
                [sg.Button('Cancelar', focus=False, size=(10,1))]]

    window = sg.Window('Registro de Optin', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break      

        finish = main(values)
        if finish == True:
            window.close() 
        else:
            print(finish)
    
if __name__ == '__main__':
    main_gui()
    
        
