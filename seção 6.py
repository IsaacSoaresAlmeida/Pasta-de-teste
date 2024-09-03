# if ,else e elif:
"""
nota1 = float(input( "Digite a primeira nota"))
nota2 = float(input( " Digite a segunda nota"))
nota3 = float(input( "Digite a terceira nota"))

total = nota1 + nota2 + nota3 

média = total/3

if média >= 7:
    print( 'Parabéns, voce foi aprovado')

elif média <= 4:
    print( 'Reprovado')

else:
    print( 'Recuperação')
"""

# Operadores Logicos:

renda_minima_5mil= True 
nome_limpo = True
"""
if renda_minima_5mil and nome_limpo:
    print( "Financiamento aprovado")
else:
    print("Financiamento negado")
"""
"""
renda = float(input( "Digite o valor de sua renda"))
cpf_limpo = input( "Digite seu CPF")

if renda >= 5000 and cpf_limpo < 8:
    print( "Financiamento aprovado")
else:
    print( "Financiamento reprovado")
"""

# Multiplos operadores de comparação:
'loja de revenda de produtos'

valor_produto = 20
"""
if 20 >=  valor_produto <= 40:          OU        valor_produto >= 20 and valor_produto < 40:
    print("Produto aceito")
else:
    print("Produto negado")
"""

# For loop em numero ex( imprimir de 1 a 100):
"""
for numero in range(1, 6000, 2):
    print(numero)
"""
# For loop para str:

palavra = 'Roupa'
"""
for letra in palavra:
    print(letra)
"""
# Junto com Formated Strings:

palavra = 'Lasanha'
"""
for letra in palavra:
    print(f'{letra} esta dentro da palavra {palavra}')
"""
# For loop com if else ex:( Enviar email  com os detalhes da compra online, com no maximo 3 tentativas para compras realizadas)
#break : pula fora do loop se sor true

compra_confirmada = True
dados_compra = 'Compra no valor de R$ 300 e entrega confirmada'
"""
for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para o seu email')
        break
else:
    print('Falha na compra')
"""
#  Nested loops ( Loop dentro de um Loop)
"""
for numero1 in range(1,6):
    print('Produto'+ str(numero1))
    for numero2 in range(5):
            print(numero1,numero2)
"""
# for loop semparando str
"""
palavra = input('Dige qualquer palavra')

for space in palavra:
    print(f' {space}' , end= '')
"""

# Quadrado 6x6
"""
linhas = 6
colunas = 6
simbolo = '0'

for l in range(6):
    for c in range(6):
          print(simbolo, end='')
    print()
"""

# Criar uma promoção para um produto no valor de 500 reais com While loop
"""
valor = 500
dia = 0

while valor > 100:
    dia += 1
    valor -= 5
    print(f'O produto no dia {dia} custara R${valor}')
"""
 
#  POR FAVOR REVER ESSA COISA( PROMOÇÃO RELAMPAGO DA KABUM)
"""
produto = 'memoria ram'
estoque = 200
minutos  = 1

while estoque > 1:
    minutos  += 1
    estoque -= 1
    print(f'Ainda possui no estoque {estoque} de {produto}, o produto foi atualizado ah { minutos} minutos')
"""
 # Operador ternario ex : Idade para votar
"""
idade_minima = 18
idade = int(input("Por favor, digite sua idade: "))

if idade >= idade_minima:
    print('Você está apto a votar')
else:
    print(f'Para votar você precisa completar a idade mínima de {idade_minima} ')
"""
        # OU

idade_minima = 18
idade = int(input("Por favor, digite sua idade: "))

resultado = 'Voto permitido' if idade >= idade_minima else f'Complete a idade minima para votar,{idade_minima} anos.'

print(resultado)
 







