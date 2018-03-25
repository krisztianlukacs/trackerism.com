# Raspberry Pi 3 B+
# CPU Tempreture Reader
# Krisztian Lukacs 2018.03.25. Budapest


# cd /sys/class/thermal/thermal_zone0
# cat temp

import io 

f = open("/sys/class/thermal/thermal_zone0/temp", "r")
t = f.readline ()

cputemp = "CPU temp: "+t

print (cputemp)

exit