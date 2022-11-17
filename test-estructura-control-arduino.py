#----------------------------------------------------------------------------------------
#importar las librerias necesarias
from pyfirmata import Arduino
import time
import cv2
#----------------------------------------------------------------------------------------
#importar las funciones de los archivos necesarios
from testdeteccionEPI import deteccionEPI
from testdeteccionRFID import deteccionRFID
from testAperturaCerradura import aperturaCerradura
#----------------------------------------------------------------------------------------

count = 0 #variable para contar el tiempo maximo de espera de deteccion de EPI
detectEPI = False #variable de control para el acceso por EPI
detectRFID = False #variable de control para el acceso por RFID
detectBoton = False #variable de control para la apertura con boton


#Leer el puerto en el que se encuentra Arduino conectado
board = Arduino("/dev/ttyACM0")


#apagar todos los LEDs
board.digital[13].write(0)
board.digital[12].write(0)
board.digital[11].write(0)
board.digital[10].write(0)

#puerto de prueba para sensor de movimiento
board.digital[7].write(0)
#puerto de prueba para boton de apertura
board.digital[6].write(1)

while True:
    #lectura de puertos importantes de la placa Arduino
#    board.digital[8].read()
    
    
#    if (board.digital[8].read() == 1): #lectura de puerto de sensor de movimiento
#--------------------Funcion de deteccion EPI-------------------------------------------------------------------- 
    if (board.digital[7].read() == 1):
        while (detectEPI != True and count <20): #mientras el valor de estado no sea true o pasen 20 seg
            detectEPI = deteccionEPI()  #funcion de deteccion de mascara
            if (detectEPI == True):
                print("Bienvenido EPI")
                board.digital[13].write(1)
                aperturaCerradura()
                board.digital[13].write(0)
            count = count + 1
#-------------------Funcion de deteccion RFID---------------------------------------------------------------------
    detectRFID = deteccionRFID()
    if(detectRFID == True):
        print("Bienvenido RFID")
        board.digital[12].write(1)
        aperturaCerradura()
        board.digital[12].write(0)
#----------------------------------------------------------------------------------------
    if (board.digital[6].read() == 1):
        print("Apertura por Boton")
        aperturaCerradura()
    
    board.digital[11].write(1)
    time.sleep(0.5)
    board.digital[11].write(0)
    time.sleep(0.5)


time.sleep(5)
board.digital[13].write(0)
board.digital[12].write(0)
#        deteccionGuantes()  #funcion de deteccion de guantes
    
    
