#Escriba una funci�n que reciba un string como par�metro y retorne el string, pero con cada elemento que estuviese en may�sculas reemplazado por "$". Asuma que el string consistir� solamente de letras.

def reemplazo(string):
  res = ""
  mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for s in string:
    if s in mayusculas:
      s = "$"
    res = res + s
  return res # aqu� debes retornar el resultado

a = "Viva la Vida"

x = reemplazo(a)
print(x)