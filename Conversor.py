# Online Python compiler (interpreter) to run Python online.

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter pra BINÁRIO
[ 2 ] Converter pra OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao= int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
      print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
    