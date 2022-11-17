from pyfirmata import Arduino
import time

board = Arduino("/dev/ttyACM0") #Puerto de la placa Arduino Leonardo


while True:

    numpuerto = int(input('Que LED quiere encender: '))
    if (numpuerto == 13):  
        board.digital[13].write(1)
        print ("Encendiendo Puerto ", numpuerto)
        time.sleep(0.2)
        break
    if (numpuerto == 12):
        board.digital[12].write(1)
        print ("Encendiendo Puerto ", numpuerto)
        time.sleep(0.2)
        break
while True:
    n = int(input('Desea apagar el LED? '))
    if (n ==1):
        board.digital[13].write(0)
        board.digital[12].write(0)
        print("Adios.")
        break