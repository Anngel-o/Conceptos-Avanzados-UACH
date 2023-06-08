﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Hilos2
{
    class Program
    {
        private static bool ejecutar = true; //variables estáticas
        private static int conteo = 0;
        private static ManualResetEvent signal = new ManualResetEvent(false);
        //señal que permanece en false hasta que se mande a activar
        //nos ayuda a controlar los procesos
        static void Main(string[] args)
        {
            int a = 15; int b = 10; List<int> respu = new List<int>();
            int n = 0; bool bloq = false;

            Thread h1 = new Thread(hilo1);//se define un nuevo hilo
            Thread h2 = new Thread(hilo2);//se define un nuevo hilo
            Thread h3 = new Thread(() => suma(a, b, respu));//se define un nuevo hilo
            Thread h4 = new Thread(() => suma(a, b, respu));//se define un nuevo hilo, también puede recibir más de un parámetro
            Thread h5 = new Thread(incremento);//se define un nuevo hilo
            h1.Start(); //se inicia la ejecución del hilo
            h2.Start("USANDO HILOS CON C# ");// se inicia la ejecución del hilo (opcionalmente puede recibir un objeto)
            h3.Start();
            h4.Start();
            h5.Start();
            while (n < 150)
            {
                Console.ForegroundColor = ConsoleColor.Yellow; // cambiamos el color de las letras de terminal
                bloq = (h5.ThreadState != 0);
                Console.WriteLine("Bloqueado {0}", bloq);
                //si el hilo está esperando una señal para ejecutarse estará bloquedado (false)
                n++;
            }
            signal.Set();//el hilo continua con su proceso
            h1.Join();//hasta que el hilo se ejecute continua el siguiente
            h2.Join();
            h3.Join();
            h4.Join();
            h5.Join();
            Thread.Sleep(2000);//realiza una pausa de 2 segundos
            Console.Write("Hilo finalizado ");

            
            Console.Read();// nos permite ver la salida del programa
        }
        static void hilo1()
        {
            var random = new Random().Next(0, 100);
            Console.Write(random);
        }

        static void hilo2(object obj)
        {
            Console.Write(obj.ToString());// el hilo puede recibir un objecto al iniciar en este caso un tipo string
            for (int i = 0; i < 5; i++)
            {
                Console.Write(" Se usar hilos con c# ");
            }
        }

        static void suma(int op1, int op2, List<int> res)
        {
            Console.Write(" SUMA ");
            res.Add(op1 + op2);
            Console.Write(res);
        }

        static void resta(int op1, int op2, List<int> res)
        {
            Console.Write(" RESTA ");
            res.Add(op1 - op2);
            Console.Write(res);
        }

        static void incremento()
        {
            while(ejecutar)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                conteo+=1;
                Console.Write(Thread.CurrentThread.ManagedThreadId);
                Console.WriteLine(" -> {0}", conteo);
                if(conteo > 1000)
                {
                    ejecutar = false;
                    signal.Dispose();//no necesitamos la señal, cerramos o liberamos los subprocesos creados
                }

                //bloqueamos el hilo hasta que se mande una señal
                if(conteo == 50)
                {
                    //el programa creará 1000 números, cuando llegue al 50 se bloqueará 
                    //para después desbloquearse y seguir el proceso
                    signal.WaitOne();//espera la señal que indique que algo ha sucedido
                }
            }
        }
    }
}
