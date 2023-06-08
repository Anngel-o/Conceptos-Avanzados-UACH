import threading
import random
cuenta =0 #global porque se modificará
 ## La funcion del tipo 1 de hilo
def hilo1 ( canda ):
  n= random.randint (1 ,10) #numero aleatorio entero
  total =0
  global cuenta
  while total <=n:
   canda.acquire () #activar candado
   cuenta+=1
   canda.release () #desactivar candado
   total+=1

 ## La funcion del tipo2 para un hilo
def hilo2 ( canda ):
  n= random . randint (1 ,30)
  total =0
  global cuenta
  while total <=n:
   canda . acquire ()
   cuenta +=2
   canda . release ()
   total +=1

 ## La funcion principal del programa
def main ():
  canda = threading . Lock ()  #del tipo candado o lock
  h1= threading . Thread ( target =hilo1 , args =[ canda ])
  h2= threading . Thread ( target =hilo1 , args =[ canda ])
  h3= threading . Thread ( target =hilo2 , args =[ canda ])
  h4= threading . Thread ( target =hilo2 , args =[ canda ])
  h1. start ()
  h2. start ()
  h3. start ()
  h4. start ()
  h1. join ()
  h2. join ()
  h3. join ()
  h4. join ()
  print ("El estado final de la cuenta es:",cuenta)
 ## El punto de entrada al programa
if __name__=="__main__":
  main()