import threading
import time 

## Una funcion Hilo1
def sumale (ope1,ope2,res):
  print (" Suma")
  res. append (ope1+ope2)
  

 ## Una funcion Hilo2
def restale (ope1,ope2,res):
  print (" Resta ")
  res. append (ope1-ope2)
 

 ## La funcion principal del programa
def main ():
  a=10
  b=20
  respu=[]

  hilo1 = threading.Thread ( target =sumale , args =(a,b,respu ,))
  hilo2 = threading.Thread ( target = restale , args =(a,b,respu ,))
  
 #Se inician los hilos
  hilo1.start ()
  hilo2.start ()
  
  print("Resultados")
  print ( respu )
 ## El punto de entrada al programa
if __name__=="__main__":
  main()