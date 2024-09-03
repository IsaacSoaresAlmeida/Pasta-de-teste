# Isaac tem 20 anos e mora na cidade de Teresina.
""""
nome = "Isaac"
idade = 20
idade = str(idade)
cidade = "Teresina"

print(nome + " tem " + idade + " anos de idade e mora em " + cidade + ".")
"""
#Adicionando input
"""
nome = input ("Qual o seu nome ? : ")
idade = input ( "Qual a sua idade ? : ")
idade = str(idade)
cidade = input ("Em qual cidade você mora ? : ")
 
print( nome + " tem " + idade + " anos de idade " + " e mora na cidade de " + cidade)
"""

#João é casado com Maria e possui 3 filhos, e ele pretende se mudar para uma casa maior
"""
nome1 = "João"
nome2 = "Maria"
filhos = 3
filhos = str(filhos)

print(nome1 + " é casado com " + nome2 + " e possui " + filhos + " filhos" " e ele pretende se mudar para uma casa maior ")
"""
# Calculando com Imput
""""
ano_nascimento = input("Em que ano voce nasceu ? : ")
idade = 2024 - int(ano_nascimento)

print('Voce tem ' + str(idade) + ' anos')
"""
# Slice
"""
Valores = 135.65
#index    012345
Valores = str(Valores)

print(Valores[2:4])
"""

#  Formated Strings

# O Isaac Soares é um excelente lutador de jiujitsu
"""
nome = "Isaac"
sobrenome = "Soares"
profissão = "lutador de jiujtsu"

print(f'O {nome} {sobrenome} é um excelente {profissão}')
"""

# Metodos para Strings