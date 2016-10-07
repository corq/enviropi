# Based heavily on https://blog.bartbania.com/raspberry_pi/temperature-log-howto/

import rrdtool
import time, sys

from subprocess import PIPE, Popen
from envirophat import light, weather

dataFile = "environment.rrd"
FACTOR = 1.3

def get_environment():
    data = {'boardTemp': weather.temperature(), 'atm': weather.pressure(), 'light': light.light()}
    data['cpuTemp'] = get_cpu_temperature()
    data['calibTemp'] = data['boardTemp'] - ((data['cpuTemp'] - data['boardTemp'])/FACTOR)

    print data
    return data

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

def export_data():
    print "Exporting data..."
    rrdtool.xport("--start",
            "now-1h",
            "--end",
            "now",
            "DEF:a="+dataFile+":cpuTemp:AVERAGE",
            "DEF:b="+dataFile+":boardTemp:AVERAGE",
            "DEF:c="+dataFile+":calibTemp:AVERAGE",
            "DEF:d="+dataFile+":atm:AVERAGE",
            "DEF:e="+dataFile+":light:AVERAGE",
            'XPORT:a:"CPU Temp"',
            'XPORT:b:"Board Temp"',
            'XPORT:c:"Calibrated Temp"',
            'XPORT:d:"Atmospheric Pressure"',
            'XPORT:e:"Light"')

if __name__ == '__main__':
    count = 0
    while True:
        try:
            print 
            if (count % 5) == 0:
                export_data()
            data = get_environment()
            dataString = "N:{cpuTemp}:{boardTemp}:{calibTemp}:{atm}:{light}".format(**data)
            # print dataString
            rrdtool.update(dataFile, dataString)
            time.sleep(60)
            count += 1
        except KeyboardInterrupt:
            print "Exiting..."
            sys.exit()
