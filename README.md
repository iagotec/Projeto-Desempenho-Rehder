# 🏫 Sistema de Monitoramento de Presença Escolar

Este projeto foi desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) do curso de Análise e Desenvolvimento de Sistemas. Ele tem como objetivo automatizar o controle de presença em salas de aula e gerar indicadores visuais de desempenho semanal e mensal.

## 🎯 Objetivo

Criar um sistema interativo que permita:

- Registrar presenças semanais por sala.
- Calcular o desempenho com base nas quatro semanas do mês.
- Classificar as salas com base em indicadores:
  - 🟢 **Bom** (≥ 75%)
  - 🟡 **Médio** (≥ 50% e < 75%)
  - 🔴 **Ruim** (< 50%)
- Apontar a sala vencedora do mês com premiação.

## 🛠 Tecnologias utilizadas

- Python 3
- PySimpleGUI (interface gráfica)
- SQLite (opcional para persistência)
- Lógica condicional e estrutura de repetição

## 📁 Estrutura do Projeto

| Arquivo         | Descrição                                           |
|------------------|-----------------------------------------------------|
| `presencas.py`   | Código principal com interface e lógica de cálculo |
| `README.md`      | Descrição do projeto                               |

## 🚀 Como executar

1. Instale as dependências:

```bash
pip install PySimpleGUI
