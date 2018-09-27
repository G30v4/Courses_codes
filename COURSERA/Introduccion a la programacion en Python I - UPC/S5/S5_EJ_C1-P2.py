#Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero, pero con el segundo string intercalado entre cada letra del primero.

def intercalar(string_a, string_b):
  res = ""
  for s in string_a:
    res = res + s + string_b
  return res # aquí debes retornar el resultado

a = "paz"
b = "so"

x = intercalar(a,b)
print(x)