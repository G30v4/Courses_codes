#Metodo de Euclides para obtener el MCD con algoritmo recursivo
def mcd(n1, n2):
  if n1 > n2:
    if n2==0:
      return print(n1)
    else:
      return mcd(n2, n1%n2)
  else:
    if n1==0:
      return print(n2)
    else:
      return mcd(n1, n2%n1)

mcd(15,10)