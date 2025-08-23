# MANUAL PYTHON

print("Ola, mundo!") # imprime na tela mensagens - escreva a mensagem ola mundo
print(5+3) # exemplo 2, sem aspas imprime o resultado da soma e nao uma mensagem - escreva o resultado da soma

nome = "Biatrice" # variavel
idade = 20 # variavel

if idade >= 18: # condicoes
    print("Maior de idade")
else: 
    print("Menor de idade")

for i in range(6): # lacos de repeticao
   print(i) 

r = 'S' # declaracao variavel
while r == 'S': # enquanto r receber s
    n = int(input('Digite um valor: ')) # declaracao de variavel
    r = str(input('Quer continuar? [S/N]')).upper() # upper = case sensitive  / enquanto responder sim, quer continuar.
print('FIM') 