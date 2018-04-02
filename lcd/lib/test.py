import lcddriver
import time
import io 

lcd = lcddriver.lcd()

lcd.lcd_clear()

lcd.lcd_display_string("Sziasztok",1)
lcd.lcd_display_string("Anya, Leon, Ama",2)

time.sleep(1)

lcd.lcd_clear()
f = open("/sys/class/thermal/thermal_zone0/temp", "r")
t = f.readline ()

cputemp = "CPU temp: "+t

lcd.lcd_display_string(cputemp,1)

time.sleep(5)

lcd.lcd_backlight("off")

exit