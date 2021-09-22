from PySimpleGUI import PySimpleGUI as sg


#Layout
sg.theme('dark')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario',)],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de login', layout)

#Ler os eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Entrar':
        if valores['usuario'] == 'Gustavo' and valores['senha'] == '12345':
            print('Bem vindo ')