#Llamar a funcion hola
#Función hola
from termcolor import colored
import os
#from os import chdir no funcionó
import sys #path
os.system("color")
#os.chdir("C:\\PGRMAS\\python\\3Subprogramas") #cambio de directorio de la función y no funciona

sys.path.append("C:\\PGRMAS\\python\\3Subprogramas") #cambio de directorio de la función y funcionó
from Fhello import hola

#from Fhola import hola    #from file import function

def main():
    
    print("             ")
    mengano=input("Hola, ¿Cual es tu nombre?: ")
    hola(mengano)

    #Le dices a python cual es la entrada ppal
if __name__=="__main__":
  main()