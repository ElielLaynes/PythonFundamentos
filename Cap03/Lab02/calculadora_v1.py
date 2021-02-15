# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Calculadora Python *******************\n")

print('Selecione o número da operação desejada:')

print('''
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
 ''')
# Inserção da opção de calculo desejado
opcao = int(input('Digite sua opção (1 | 2 | 3 | 4): '))

# Inserção dos números para fazer o calculo
num1 = int(input('\nDigite o Primeiro Número: '))
num2 = int(input('\nDigite o Segundo Número: '))

# Bloco if para fazer as operaçãos dos calculos
if opcao == 1:
    print(f'\nA Soma de {num1} + {num2} é: {num1 + num2}')
elif opcao == 2:
    print(f'\nA Subtração de {num1} - {num2} é: {num1 - num2}')
elif opcao == 3:
    print(f'\nA Multiplicação de {num1} x {num2} é: {num1 * num2}')
elif opcao == 4:
    print(f'\nA Divisão de {num1} / {num2} é: {num1 / num2}')
else:
    if opcao > 4:
        print(f'\nOpção Inválida!')
# Print para pular uma linha e deixar mais legível na hora do print dos dados no Terminal        
print()

