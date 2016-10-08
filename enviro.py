# Based heavily on https://blog.bartbania.com/raspberry_pi/temperature-log-howto/

import rrdtool
import time, sys

from subprocess import PIPE, Popen
from envirophat import light, weather, leds

dataFile = "/home/shearna/repos/enviropi/environment.rrd"
FACTOR = 1.3

def get_environment():
    data = {'boardTemp': weather.temperature(), 'atm': weather.pressure(), 'light': light.light()}
    data['cpuTemp'] = get_cpu_temperature()
    data['calibTemp'] = data['boardTemp'] - ((data['cpuTemp'] - data['boardTemp'])/FACTOR)

    # print data
    return data

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

if __name__ == '__main__':
    print "Starting..."
    while True:
        try:
            data = get_environment()
            dataString = "N:{cpuTemp}:{boardTemp}:{calibTemp}:{atm}:{light}".format(**data)
            # print dataString
            rrdtool.update(dataFile, dataString)
            time.sleep(60)
        except KeyboardInterrupt:
            print "Exiting..."
            sys.exit()
