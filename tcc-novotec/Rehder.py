import PySimpleGUI as sg
import sqlite3
import back
import random


def navbar():
    layout= [
        [sg.Text('Bem vindo')],
        [sg.Button('ENTRAR'),sg.Button('SAIR')]
    ]

    window = sg.Window('Presença Rehder', layout, size=(500,100), element_justification='center')
    
    while True:
        button, values =  window.read()

        if button == sg.WIN_CLOSED:
            break
        
        if button == 'ENTRAR':
            window.close()
            corpo()

        if button == 'SAIR':
            window.close() 


def corpo():
    sala=back.listabox()
    
    def calcular_desempenho(presenca,total):
        if total==0:
            return "RUIM"
        capacidade_semanal= total*5
        percentual= (presenca/capacidade_semanal)*100
        print(f"presença: {presenca}, Total: {total}, Percentual: {percentual:.2f}")
        
        if percentual >= 75 :
            return "BOM"
        elif percentual>= 50:
            return "MÉDIO"
        else:
            return "RUIM"
        

    def desempenho_final(sem1,sem2,sem3,sem4,total):
        if total==0:
            return "RUIM"
        capacidade_mensal= total*20
        presencas_totais = sem1 +sem2+sem3+sem4
        percentual = (presencas_totais/capacidade_mensal)*100

        if percentual>= 75:
            return 'BOM'
        elif percentual>= 50:
             return 'MEDIO'
        else:
             return 'RUIM'
    
    def formatar_lista():
         salas = back.listabox()
         lista_formatada = []
         for sala in salas:
            nome, sem1,sem2,sem3,sem4,total=sala
            desempenho1 = calcular_desempenho(sem1,total)
            desempenho2 = calcular_desempenho(sem2,total)
            desempenho3 = calcular_desempenho(sem3,total)
            desempenho4 = calcular_desempenho(sem4,total)
            desempenho_geral= desempenho_final(sem1,sem2,sem3,sem4, total)
            lista_formatada.append(f"{nome}             {desempenho1}              {desempenho2}             {desempenho3}            {desempenho4}            {desempenho_geral}"      )
         
         return lista_formatada

    def melhor_sala():
        salas = back.listabox()
        melhor=None
        melhor_desempenho= -1

        for sala in salas:
            nome,sem1,sem2,sem3,sem4, total=sala
            if total>0:
                desempenho_geral = (sem1+sem2+sem3+sem4)/(4 *total)
                if desempenho_geral > melhor_desempenho:
                    melhor=nome
                    melhor_desempenho= desempenho_geral
        if melhor is None:
            return None,None
        return melhor_desempenho, melhor 
    

    def sortear():
        premios = ["passeio", "cinema", "Ed, física", "pequenique"]
        return random.choice(premios)

    layout= [
        [sg.Text('Digite a sala'), sg.InputText('', key= '-Sala-'),sg.Push()],
        [sg.Text(f'Quantos alunos na sala? '), sg.InputText('', key= '-quant-'),sg.Push()],
        [sg.Push(), sg.Text('Digite quantos alunos vieram em cada semana:'), sg.Push()],
        [sg.Text('alunos na 1 semana'), sg.InputText('', key= '-Sem1-')],
        [sg.Text('alunos na 2 semana'), sg.InputText('', key= '-Sem2-')],
        [sg.Text('alunos na 3 semana'), sg.InputText('', key= '-Sem3-')],
        [sg.Text('alunos na 4 semana'), sg.InputText('', key= '-Sem4-')],
        [sg.Text('Desempenho mensal:',size=(20,1)),sg.Text('Desempenho mensal',key= '-finaly-')],
        [sg.Button('ADICIONAR'), sg.Button('VENCEDOR')],
        [sg.Text('SALA          SEMANA-1   SEMANA-2   SEMANA-3   SEMANA-4   DESEMPENHO')],
        [sg.Listbox( sala, size=(80,20), key= '-box-')],
        [sg.Button('DELETAR'),sg.Button('SAIR')]
    ]

    window = sg.Window('Presença Rehder', layout)
    
    while True:
        button, values =  window.read()

        if button == sg.WIN_CLOSED:
            break
        

        if button == 'SAIR':
            window.close() 

        

        if button == 'ADICIONAR':
            sala= values['-Sala-']
            try:
                chamada=int(values['-quant-'])
                sem1= int(values['-Sem1-'])
                sem2= int(values['-Sem2-'])
                sem3= int(values['-Sem3-'])
                sem4= int(values['-Sem4-'])

                desempenho_geral= desempenho_final(sem1,sem2,sem3,sem4, chamada)
                window['-finaly-'].update(desempenho_geral)
            
            

                if sala:
                    back.adicionar(sala,sem1,sem2,sem3,sem4,chamada)
                    window['-box-'].update(formatar_lista())
                    window['-Sala-'].update('')
                    window['-quant-'].update('')
                    window['-Sem1-'].update('')
                    window['-Sem2-'].update('')
                    window['-Sem3-'].update('')
                    window['-Sem4-'].update('')
            except ValueError:
                sg.popup('por favor, insira valores válidos!')

        if button == 'VENCEDOR':
            desempenho,vencedor= melhor_sala()
            if vencedor:
                    if desempenho is not None:
                        premio=sortear()
                        sg.popup(f"A sala vencedora é: {vencedor}\nDesempenho: {desempenho * 100:.2f}%\nPrêmio: {premio}")

                    else:
                        sg.popup(f"desempenho inválido")
                    
            else:
                sg.popup("Nenhuma sala com bom desempenho para ser vencedora")
                    
        
            
navbar()
