# Serial UART Communication on Raspberry Pi

# import serial

# ser1 = serial.Serial('COM8', 9600)
# ser1.write('s'.encode())


import time
import serial

print "Starting program"

ser = serial.Serial('/dev/ttyAMA0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)
try:
    ser.write('Hello World\r\n')
    ser.write('Serial Communication Using Raspberry Pi\r\n')
    ser.write('By: Embedded Laboratory\r\n')
    print 'Data Echo Mode Enabled'
    while True:
        if ser.inWaiting() > 0:
            data = ser.read()
            print data
        
except KeyboardInterrupt:
    print "Exiting Program"

except:
    print "Error Occurs, Exiting Program"

finally:
    ser.close()
    pass
