import sys #Librería con instrucciones del S.O.
from math import factorial
import os #funciones del SO
from termcolor import colored
#pip install termcolor 

def main():
  x=0
  y=0
  z=0
  i=0
  exp=0
  res=0.0
  ResF=0
  opc=0
  Nombre=["Selma","Marge","Maggie","Patty","Liza"]
  os.system("color")

  while(opc !=8): #mientras sea diferente a 8
    print("                                    ")
    print("Opciones: ")
    print("1: División")
    print("2. División con warning ")
    print("3. División con terminación del pgma")
    print("4. Nombre")
    print("5:Interrumpe el ciclo")
    print("6: Factorial Usuario")
    print("7: Factorial Sistema")
    print("8: Salir")
    print("                                     ")
    opc=int(input("¿Opción ?: "))
    #-------División sin excepción---------
    if (opc == 1):
       x=float(input("Teclea  dividendo: "))
       y=float(input("Teclea divisor: "))  
       res=x/y
       print(colored("Resultado: ","yellow"),res)
       print("                                     ")
    #---------División con excepción-------   
    elif (opc == 2):
       x=float(input("Teclea  dividendo: "))
       y=float(input("Teclea divisor: "))
       try:
           res=x/y
           print(colored(" ------------------ ","green"))
           print(" Resultado:  ",res)
       except:
           print(colored(" ╔══════════════════════════╗ ","red"))
           print(colored(" ║  Error: Divisor en cero  ║  ","red"))
           print(colored(" ╚══════════════════════════╝ ","red"))
   #-------------------Se termina el pgma----------------------
    elif opc == 3:
       x=float(input("Teclea  dividendo: "))
       y=float(input("Teclea divisor: "))
       try:
           res=x/y
           print(" ------------------ ")
           print(" Resultado:  ",res)
       except:
           print(colored(" ╔══════════════════════════╗ ","red"))
           print(colored(" ║  Error: Divisor en cero  ║  ","red"))
           print(colored(" ╚══════════════════════════╝ ","red"))
           sys.exit(1) #=1 sale del pgma , =0 salida exitosa
    elif opc == 4:
        z=int(input("teclea un número entre 1 y 5: "))
        try:      
            print(Nombre[z-1])
        except IndexError:
            print(colored(" ╔══════════════════════════╗ ","red"))
            print(colored(" ║         No existe        ║  ","red"))
            print(colored(" ╚══════════════════════════╝ ","red"))
        else:
            print(" Por si las otras opciones no se realizan")
        finally:
             print("Gracias por su tiempo")
    #-----------Excepción: Interrumpe un ciclo---------
    elif opc == 5:
        z=int(input("teclea un número mayor a 1"))
        try:      
             while z>1:
              print(colored(" \m/(>.<)\m/  ","yellow"))
              print(i)
              i=i+1
        except KeyboardInterrupt:
            print(colored(" ╔══════════════════════════╗ ","red"))
            print(colored(" ║ Interrupción por usuario ║  ","red"))
            print(colored(" ╚══════════════════════════╝ ","red"))
   #----------------6 : FACTORIAL ASSERT ------------------------         
    elif opc==6:
        z=int(input("Teclea el número: "))
          #si la condición NO es verdadera:
        assert z>0,colored("No teclear número negativos","red")
        ResF=factorial(z)
        print(colored(" Factorial: ","magenta",),ResF)
 #----------------7 : FACTORIAL EXISTENTE ------------------------         
    elif opc==7:
        z=int(input("Teclea el número: "))
        try:
           ResF=factorial(z)
           print("tecleado: ",ResF)
           print(colored(" Factorial: ","blue",),ResF)
        except:   
          #usando una existente
          raise ValueError(colored("¿UH?","red"))      
    else:   
           print(colored(" *********************   ","green") )
           print(colored("    VUELVAS PRONTOS   ","green") )
           print(colored(" *********************   ","green") )
    

if __name__=="__main__":
  main()