from multipledispatch import dispatch 
import numpy as np
#Matrices en Python
#>pip install numpy
#última versión
#>python.exe -m pip install --upgrade pip

#Sobrecarga de funciones


@dispatch(float,float,float)
def Funecu(a,b,c):
    coef=[a,b,c]
    resul=np.roots(coef)
    return resul

@dispatch(float,float,float,float)
def Funecu(a,b,c,d):
    coef=[a,b,c,d]
    resul=np.roots(coef)
    return resul

@dispatch(float,float,float,float,float)
def Funecu(a,b,c,d,e):
    coef=[a,b,c,d,e]
    resul=np.roots(coef)
    return resul

def main():
  #ecu=0
  x1=0
  x2=0
  x3=0
  x4=0
  Terind=0
  YN="Y"
  while(YN == "Y" or YN == "y"):
    print("Opciones: ")
    print("1: Ecuación de 2do grado ")
    print("2: Ecuación de 3er grado")
    print("3: Ecuación de 4to grado")
    print("4: tengo hambre")
    print("   ")
    opcion=int(input("¿Opción ?: "))
    if (opcion == 1):
      print("2° grado, Tres coeficientes: ")
      x1=float(input ("coeficiente 1: x^n "))
      x2=float(input ("coeficiente 2: x^n-1 "))
      Terind=float(input ("coeficiente 3: Término independiente "))
      resultado=Funecu(x1,x2,Terind) #Llama a la función
      print("   ")
      print(resultado)
      print("   ")
    elif(opcion == 2) :
      print("3° grado, Cuatro coeficientes: ")
      x1=float(input ("coeficiente 1: x^n "))
      x2=float(input ("coeficiente 2: x^n-1 "))
      x3=float(input ("coeficiente 3: x^n-2 "))
      Terind=float(input ("coeficiente 4: Término independiente "))
      resultado=Funecu(x1,x2,x3,Terind)
      print("   ")
      print(resultado)
      print("   ")
    elif(opcion == 3) :
      print("4° grado, Cinco coeficientes: ")
      x1=float(input ("coeficiente 1: x^n "))
      x2=float(input ("coeficiente 2: x^n-1 "))
      x3=float(input ("coeficiente 3: x^n-2 "))
      x4=float(input ("coeficiente 4: x^n-4 "))
      Terind=float(input ("coeficiente 5: Término independiente "))
      resultado=Funecu(x1,x2,x3,x4,Terind)
      print("   ")
      print(resultado)
      print("   ")
    else:
      print("    ")  
      YN=input("¿Desea continuar? Y/N: ")
      print(YN)
      print("   ")
      print("ADIÓS")

if __name__=="__main__":
  main()
