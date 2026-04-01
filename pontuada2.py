import os

os.system('cls')

#lista dos exames
exames = [
    ['Hemograma Completo', 50.00],
    ['Raio-X', 110.00],
    ['Ultrassonografia', 70.00],
    ['Eletrocardiograma', 60.00],
    ['Tomografia', 270.00],
    ['Ressonância Magnética', 400.00],
    ['Exame de Glicose', 25.00]  
]

total = 0
pedidos = []

while True:
    print('''
============== EXAMES ================
          
0 - Finalizar Atendimento       
1 - Hemograma Completo        R$50,00
2 - Raio-X                    R$110,00
3 - Ultrassonografia          R$70,00
4 - Eletrocardiograma         R$60,00
5 - Tomografia                R$270,00
6 - Ressonância Magnética     R$400,00
7 - Exame de Glicose          R$25,00
          
=======================================
''')
#escolhendo exames
    opcao = int(input('Escolha o exame: '))
    if opcao == 0:
        break

    elif 1 <= opcao <= len(exames):
        nome = exames[opcao-1][0]
        preco = exames[opcao-1][1]
        
        pedidos.append((opcao, nome))
        total += preco
        
        print(f'{nome} adicionado!')
    else:
        print('Opção inválida!')

    continuar = input('Deseja adicionar mais um exame? (s/n): ').lower()

    if continuar != 's':
        break

#escolhendo pagamento
print('''
============= PAGAMENTO ===============
1 - Convênio (15% de desconto)
2 - Particular (Sem desconto)
3 - Cartão de crédito (8% de acrescimo)          
=======================================
''')

#forma de pagamento
pagamento = int(input('Escolha a forma de pagamento: '))

desconto = 0
acrescimo = 0

#desconto/acrescimo
if pagamento == 1:
    desconto = total * 0.15
    total_final = total - desconto
    forma = 'Convênio'

elif pagamento == 2:
    total_final = total
    forma = 'Particular'

elif pagamento == 3:
    acrescimo = total * 0.08
    total_final = total + acrescimo
    forma = 'Cartão de crédito'

else:
    print('Forma de pagamento invalida! Prosseguindo pagamento sem alrteração')
    total_final = total
    forma = 'Indefinida'

#resultado final
print('\n===== RESUMO =====')

print('\nExames escolhidos:')
for codigo, nome in pedidos:
    print(f'{codigo} - {nome}')

print(f'\nSubtotal: R${total:.2f}')
print(f'Forma de pagamento: {forma}')
print(f'Desconto: R${desconto:.2f}')
print(f'Acrescimo: R${acrescimo:.2f}')
print(f'TOTAL FINAL: R${total_final:.2f}')