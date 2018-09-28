#Metodo que retorna el exponente de potencia de 2, menor o igual a "n".
def exponente(n):
  x=0
  while n > 1:
    n = n//2
    x+=1
  return print(x)

exponente(32)