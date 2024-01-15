logica_de_baixa_de_quantidades = """
Fazer query de documentos atendidos uma vez por dia, pegando todas 
as vendas e dando baixas na respectivas quantidades dos produtos
se hover na observação a key="promo victor"
e lancar a venda na tabela comissao fazer verificação de devolução e cancelamento
"""

alarme_de_aviso_validade = """
enviar email quando produtos estiverem procimos do vencimento
"""

cadastrar_vencidos_nosistema="""
verificar se todos os vencimentos ativos
estao com os respectivos produtos com (PROMO)
na descrição e tambem se os vencimentos inativos estao sem
"""

base_de_dados = """
validades:[

uid PK
cdprincipal FK
dtvalidade date not null
qtestoque integer not null
stativo boolean defalt true
created_at
updated_at
]
produtos:[

iddetalhe
cdprincipal PK
dsdetalhe varchar(40) not null
imagem nullable

]
comissao: [

iddocumento not null
iddocumentoitem not null
cdorcamento not null
cdprincipal not null
cdchamada not null
dsvendedor not null
vltotal float not null
ispaid boolean defalt False
created_at
updated_at

]
"""
routes = """
"/" = {
menu principal que te envia para 
lançamento de vencimentos (100% mobile)
listagem de vencimentos ativos 
listagem de valor a ser pago de comissionamento por vendedor
}
"""