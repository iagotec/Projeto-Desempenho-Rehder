import sqlite3

# Conexão com o banco
dbase = sqlite3.connect('registros_semanais.db')
u = dbase.cursor()

# Criação da tabela
u.execute('''CREATE TABLE IF NOT EXISTS salas_de_aula (
                SALA TEXT PRIMARY KEY NOT NULL,
                SEMANA_1 INT,
                SEMANA_2 INT,
                SEMANA_3 INT,
                SEMANA_4 INT,
                MES INT)''')
dbase.commit()

def adicionar(SALA, S1, S2, S3, S4, MES):
    try:
        u.execute(
            '''INSERT OR REPLACE INTO salas_de_aula 
               (SALA, SEMANA_1, SEMANA_2, SEMANA_3, SEMANA_4, MES)
               VALUES (?, ?, ?, ?, ?, ?)''',
            (SALA, S1, S2, S3, S4, MES)
        )
        dbase.commit()
    except sqlite3.Error as e:
        print("Erro ao inserir: ", e)

def listar():
    u.execute("SELECT * FROM salas_de_aula")
    return u.fetchall()

def deletar(SALA):
    u.execute("DELETE FROM salas_de_aula WHERE SALA = ?", (SALA,))
    dbase.commit()

def obter_dados(SALA):
    u.execute("SELECT * FROM salas_de_aula WHERE SALA = ?", (SALA,))
    return u.fetchone()
