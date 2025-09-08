
""" 
introducao ao try/except
try --> tentar executar o codigo
except --> ocorreu algum erro ao tentar executar
"""


numero_str = input("Vou dobrar o numero que voce digitar: ")

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print('Voce nao digitou um numero inteiro')



if numero_str.isdigit():
   
    print('Fim do calculos')

else:

    print('Fim do calculo')


