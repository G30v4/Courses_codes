#Escriba una funci�n que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.

def ocurrencias(string):
  ceros = 0 
  unos = 0
  for s in string:
    if s == "1":
      unos += 1 
    else:
      ceros += 1
  return unos - ceros # aqu� debes retornar el resultado

a = "110001100101100"

x = ocurrencias(a)
print(x)