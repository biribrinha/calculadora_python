def decimal_para_binario(decimal):
    """
    Função que converte um número decimal para binário.
    """
    if decimal == 0:
        return '0'
    else:
        binario = ''
        while decimal > 0:
            resto = decimal % 2
            binario = str(resto) + binario
            decimal //= 2
        return binario


def binario_para_decimal(binario):
    """
    Função que converte um número binário para decimal.
    """
    decimal = 0
    expoente = 0
    for digito in reversed(binario):
        decimal += int(digito) * 2 ** expoente
        expoente += 1
    return decimal


def decimal_para_hexadecimal(decimal):
    """
    Função que converte um número decimal para hexadecimal.
    """
    digitos_hex = '0123456789ABCDEF'
    hexadecimal = ''
    while decimal > 0:
        resto = decimal % 16
        hexadecimal = digitos_hex[resto] + hexadecimal
        decimal //= 16
    return hexadecimal


def hexadecimal_para_decimal(hexadecimal):
    """
    Função que converte um número hexadecimal para decimal.
    """
    digitos_hex = '0123456789ABCDEF'
    decimal = 0
    expoente = 0
    for digito in reversed(hexadecimal):
        decimal += digitos_hex.index(digito) * 16 ** expoente
        expoente += 1
    return decimal


while True:
    print("Digite 1 para converter decimal para binário")
    print("Digite 2 para converter binário para decimal")
    print("Digite 3 para converter decimal para hexadecimal")
    print("Digite 4 para converter hexadecimal para decimal")
    print("Digite 5 para sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        decimal = int(input("Digite um número decimal: "))
        binario = decimal_para_binario(decimal)
        print(f"O número {decimal} em binário é: {binario}")
        operacao = input("Digite uma operação (+, -, *, /): ")
        if operacao in ('+', '-', '*', '/'):
            segundo_numero = int(input("Digite outro número na mesma base: "))
            if operacao == '+':
                resultado = decimal + segundo_numero
            elif operacao == '-':
                resultado = decimal - segundo_numero
            elif operacao == '*':
                resultado = decimal * segundo_numero
            elif operacao == '/':
                resultado = decimal / segundo_numero
            print(f"O resultado da operação é: {resultado}")

    elif escolha == '2':
        binario = input("Digite um número binário: ")
        decimal = binario_para_decimal(binario)
        print(f"O número {binario} em decimal é: {decimal}")
        operacao = input("Digite uma operação (+, -, *, /): ")
        if operacao in ('+', '-', '*', '/'):
            segundo_numero = input("Digite outro número binário: ")
            segundo_decimal = binario_para_decimal(segundo_numero)
            if operacao == '+':
                resultado = decimal + segundo_decimal
            elif operacao == '-':
                resultado = decimal - segundo_decimal
            elif operacao == '*':
                resultado = decimal * segundo_decimal
            elif operacao == '/':
                resultado = decimal / segundo_decimal
