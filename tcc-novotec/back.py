import sqlite3
#desempenho semanais
dbase = sqlite3.connect('registros_semanais.db')
u= dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS salas_de_aula(
                    SALA PRIMARY KEY NOT NULL,
                    SEMANA_1 INT,   
                    SEMANA_2 INT, 
                    SEMANA_3 INT,
                    SEMANA_4 INT,
                    MES INT)''')

#aplica as mudanças
dbase.commit()

#escreve dentro da data base
def adicionar(SALA, SEMANA_1,SEMANA_2,SEMANA_3,SEMANA_4,MES):
    try:
        
        u.execute('''INSERT OR REPLACE INTO salas_de_aula(SALA, SEMANA_1, SEMANA_2, SEMANA_3, SEMANA_4, MES) VALUES(?, ?, ?, ?, ?, ?)''',(SALA, SEMANA_1, SEMANA_2, SEMANA_3, SEMANA_4, MES))
        dbase.commit()
    except sqlite3.Error as e:
        print('erro ao inserir dados ',e)


def listabox():
    
    u.execute('''SELECT *  FROM salas_de_aula''')
    data = u.fetchall()
    return data

#dados a sala
def obter_dados(SALA):
    u.execute('''SELECT * FROM salas_de_aula WHERE SALA = ?''', (SALA,))
    data=u.fetchone()
    return data