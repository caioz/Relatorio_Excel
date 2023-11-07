from datetime import datetime
import mysql.connector
import pandas as pd
from func import query,execucao


data = datetime.today().strftime('%Y-%m-%d')
banco1 = mysql.connector.connect(
    host="Servidor/IP",
    port="3306",
    user="report",
    password="senha",
    database="nome_banco_1")
banco2 = mysql.connector.connect(
    host="Servidor/IP",
    port="3306",
    user="report",
    password="senha",
    database="nome_banco_2"
)

mycursor_banco1 = banco1.cursor(dictionary=True)
mycursor_banco2 = banco2.cursor(dictionary=True)


myresult_pq_banco1 = execucao(mycursor_banco1,query('pq'))
myresult_pq_banco2 = execucao(mycursor_banco2,query('pq'))
myresult_pf = execucao(mycursor_banco1,query('pf'))


dados_pq = pd.concat([pd.DataFrame(myresult_pq_banco1),pd.DataFrame(myresult_pq_banco2)])
dados_pf = pd.DataFrame(myresult_pf)


escrever = pd.ExcelWriter(f"{data} - Relatório.xlsx", engine='xlsxwriter')



dados_pq.to_excel(escrever,sheet_name='PQ' ,index=False)
dados_pf.to_excel(escrever,sheet_name='PF' ,index=False)

escrever.close()

print('Concluido')
