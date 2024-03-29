import datetime
import json
import os
import dotenv
from DbConnectPostgres import DbConnectPostgres


with open('validades.txt', 'r', encoding="utf-8") as file:
    data = file.readlines()
  
results = []
vencimentos = [line.strip('\n').split(':') for line in data if line.strip()]
for item in vencimentos:
    
    if len(item[1].strip()) == 5:
        item[1] = '01/'+item[1].strip()
    item[1] = datetime.datetime.strptime(item[1].strip(), "%d/%m/%y").strftime("%Y-%m-%d")
    if len(item[0].strip()) < 6:
        item[0] = '0' * (6 - len(item[0].strip())) + item[0].strip()
    item [0] = item[0].strip()
    item [1] = item[1].strip()
    item [2] = item[2].strip()
    results.append(item)
    
contagem = {}

for item in results:
    
    valor = item[0] + item[1]
    contagem[valor] = contagem.get(valor, 0) + int(item[2])

new_result = []
for item in results:
    valor = item[0] + item[1]
    item[2] = contagem[valor]
    new_result.append(item)

lista_sem_duplicatas = []
ocorrencias ={}

for item in new_result:
    valor = item[0] + item[1]

    
    if valor not in ocorrencias:
        ocorrencias[valor] = True
        lista_sem_duplicatas.append(item)

lista_sem_duplicatas.sort(key=lambda x: int(x[0]))
dotenv.load_dotenv()
db_alterdata = DbConnectPostgres(
            os.environ['HOST'],
            os.environ['PORT'], 
            os.environ['DBNAME'], 
            os.environ['USER'], 
            os.environ['PASSWD']
        )

with db_alterdata.connect():

    query =  """
SELECT det.iddetalhe, det.cdprincipal, det.dsdetalhe, img.foto AS imagem FROM wshop.detalhe as det
LEFT JOIN wshop.detalhefoto AS img ON img.iddetalhe = det.iddetalhe
"""
    products = db_alterdata.sqlquery(query)

final = []
for val in lista_sem_duplicatas:
    prod = [p for p in products if p['cdprincipal'] == val[0]]
    prod = prod[0]
    if prod["imagem"]:
        try:
            prod["imagem"] = prod["imagem"].tobytes()
        except:
            pass
    prod["imagem"] = str(prod["imagem"]) if isinstance(prod["imagem"], bytes) else None
    
       

    final.append(
        [prod, val[1], val[2]]
    )


with open("validades_database.json", 'w') as json_file:
    json.dump(final, json_file, indent=4)