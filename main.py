#Criem um programa que recebe um numero
#O programa imprime todos os quadrados do numero de 0 até o numero
#exemplo:
#n = 5
#0
#1
#4
#9
#16
#25
n = int(input())

#Crie uma função que retorne True caso seja um ano bissexto
#E a função retorna false caso não seja
#o ano é bissexto se ele é divisivel por 4
#ele deixa de ser bissexto se ele é divisivel por 100
#mas ainda é bissexto se também é divisivel por 400
def anobissexto(ano):
  if ano % 4 != 0:
    return False
  else:
    if ano %100 == 0:
      if ano % 400 == 0:
        return True
      else:
        return False
    else:
      return True
      
    return True
    
    
print(anobissexto(2024))
print(anobissexto(2000))
print(anobissexto(1996))
print(anobissexto(96))