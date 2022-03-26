print('{:=^40}'.format(' Loja TAF '))

valortot= float(input('Qual o Valor total da sua compra? R$'))
print('''  FORMAS DE PAGAMENTO
      [1] À vista dinheiro/ PIX
      [2] À vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão
      ''')
opcao= int(input('Digite qual a opção: '))

if opcao==1:
    valorfin= valortot - (valortot*(10/100))
    
elif opcao==2:
        valorfin= valortot - (valortot*(5/100))
        
elif opcao==3:
        valorfin= valortot
        parcela= valorfin/2
        print(F'Sua compra será de R$ {parcela} parcelada 2x')
elif opcao==4:
    valorfin=valortot + (valortot*20/100)
    totparc=int(input('Digite o total de parcelas: '))
    parcela= valorfin/totparc
    print(f'O valor total ficará R$ {parcela} parcelado em {totparc} vezes.')
print(f'Sua compra de  R${valortot} vai custar R${valorfin} no final')