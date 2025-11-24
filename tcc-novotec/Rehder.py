import PySimpleGUI as sg
import back
import random

# --------- Cálculo do desempenho ----------
def calcular_desempenho(presenca, total):
    if total == 0:
        return "RUIM"
    capacidade = total * 5
    percentual = (presenca / capacidade) * 100

    if percentual >= 75:
        return "BOM"
    elif percentual >= 50:
        return "MÉDIO"
    return "RUIM"

def desempenho_final(sem1, sem2, sem3, sem4, total):
    if total == 0:
        return "RUIM"
    presencas = sem1 + sem2 + sem3 + sem4
    capacidade = total * 20
    percentual = (presencas / capacidade) * 100

    return "BOM" if percentual >= 75 else "MÉDIO" if percentual >= 50 else "RUIM"


# ---------- Montar Tabela ----------
def tabela_dados():
    salas = back.listar()
    tabela = []
    for sala in salas:
        nome, s1, s2, s3, s4, total = sala
        tabela.append([
            nome,
            calcular_desempenho(s1, total),
            calcular_desempenho(s2, total),
            calcular_desempenho(s3, total),
            calcular_desempenho(s4, total),
            desempenho_final(s1, s2, s3, s4, total)
        ])
    return tabela


# ---------- Interface ----------
def main():
    layout = [
        [sg.Text("SALA:"), sg.Input(key='SALA')],
        [sg.Text("Total alunos:"), sg.Input(key='TOTAL')],
        [sg.Text("Semana 1:"), sg.Input(key='S1')],
        [sg.Text("Semana 2:"), sg.Input(key='S2')],
        [sg.Text("Semana 3:"), sg.Input(key='S3')],
        [sg.Text("Semana 4:"), sg.Input(key='S4')],
        [sg.Button("ADICIONAR"), sg.Button("DELETAR"), sg.Button("VENCEDOR")],

        [sg.Table(
            values=tabela_dados(),
            headings=["SALA","SEM1","SEM2","SEM3","SEM4","FINAL"],
            key='TABELA',
            auto_size_columns=True,
            justification='center',
            num_rows=10
        )]
    ]

    window = sg.Window("Presença Escolar", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "ADICIONAR":
            try:
                sala = values['SALA']
                total = int(values['TOTAL'])
                s1 = int(values['S1'])
                s2 = int(values['S2'])
                s3 = int(values['S3'])
                s4 = int(values['S4'])
                back.adicionar(sala, s1, s2, s3, s4, total)
                window['TABELA'].update(tabela_dados())
            except ValueError:
                sg.popup("Valores inválidos!")

        if event == "DELETAR":
            sala = values['SALA']
            back.deletar(sala)
            window['TABELA'].update(tabela_dados())

        if event == "VENCEDOR":
            salas = back.listar()
            melhor = None
            maior = -1

            for sala in salas:
                nome, s1, s2, s3, s4, total = sala
                desempenho = (s1+s2+s3+s4) / (4*total)
                if desempenho > maior:
                    maior = desempenho
                    melhor = nome

            if melhor:
                premio = random.choice(["Cinema", "Passeio", "Ed. Física"])
                sg.popup(f"Sala vencedora: {melhor}\nDesempenho: {maior*100:.2f}%\nPrêmio: {premio}")
            else:
                sg.popup("Nenhuma sala válida.")


main()
