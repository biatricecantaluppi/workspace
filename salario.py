r = 'S' # declaracao variavel
while r == 'S': # enquanto r receber s
    salario = float(input("Informa o salario: "))

    if salario <= 3000: # se
        print("programador junior")
    elif salario > 3000 and salario <= 6000: # ou entao
        print("programador pleno")
    elif salario > 6000 and salario <= 15000: # ou entao
        print("programador senior")
    else:                                   # caso contrario
        print("gerente de projetos")

    r = input('Quer continuar? [S/N]').strip().upper() 
print('FIM!') 