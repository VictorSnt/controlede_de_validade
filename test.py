with open('validades.txt', 'r', encoding="utf-8") as file:
    data = file.readlines()
  
results = []
vencimentos = [line.strip('\n').split(':') for line in data if line.strip()]
for item in vencimentos:
    
    if len(item[1].strip()) == 5:
        item[1] = '01/'+item[1].strip()
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
for item in lista_sem_duplicatas:
    print(item)