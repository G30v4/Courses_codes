#Escriba una funci�n que reciba un string s y un n�mero n como par�metros y retorne el mismo string s pero sin el elemento en el �ndice n.

def remover_enesimo(s, n):
  txt = ""  
  # otra alternativa (txt = s[0:n] + s[n+1:len(s)])
  c = 0
  for i in s:    
    if c != n:
      txt = txt + i
    c += 1
  return txt # aqu� debes retornar el resultado

a = "Hasta luego"
n = 3

x = remover_enesimo(a,n)
print(x)