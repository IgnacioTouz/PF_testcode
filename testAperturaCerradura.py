from pyfirmata import Arduino
import time

board=Arduino("/dev/ttyACM0")
def aperturaCerradura():
    print("Cerradura Abierta")
    board.digital[10].write(1)
    time.sleep(10)
    print("Cerradura Cerrada")
    board.digital[10].write(0)
    return