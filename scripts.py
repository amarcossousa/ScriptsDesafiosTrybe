# Soluções de 3 desafios propostos

# 01 - Usa um elemento em lista para fazer operação em uma lista
# Loops, array(listas)
def tripleTheChances(chances):
    lista = []
    for cont in range(chances):
        lista.append(cont * 3)
    return(len(lista),lista)

# 02 - Usa duas condicionais e executa uma operação 
# Operadores arimentos, condicionais
def calculadoraAdicaoSubtracao(numero, outroNumero, operacao):
    if operacao == '-':
      return numero - outroNumero
    elif operacao == '+':
      return numero + outroNumero
    return 0

# 03 - Usa um loop para percorrer uma frase e conta a quantidade de letra 
# Loops, condicionais, e array
def vezesLetraAparece(frase, letra):
    cont = 0
    for quant in frase:
         if quant == letra:
             cont +=1
    return cont