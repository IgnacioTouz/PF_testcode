from pyfirmata import Arduino
import time

board = Arduino("/dev/ttyACM0")

#print(board.get_firmata_version())

loopTimes = input('How many times would you like the LED to blink: ')
print ("Blinking "+ loopTimes + " times.")

for x in range(int(loopTimes)):
    board.digital[13].write(1)
    board.digital[12].write(1)
    time.sleep(0.2)
    board.digital[13].write(0)
    board.digital[12].write(0)
    time.sleep(0.2)