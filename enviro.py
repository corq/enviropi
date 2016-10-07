# Based heavily on https://blog.bartbania.com/raspberry_pi/temperature-log-howto/

import rrdtool
import time, sys

from envirophat import light, weather

def get_environment():
    return {'temp': weather.temperature(), 'atm': weather.pressure(), 'light': light.light()}

if __name__ == '__main__':
    dataFile = "environment.rrd"

    while True:
        try:
            data = get_environment()
            print data
            dataString = "N:%f:%f:%d" % (data['temp'], data['atm'], data['light'])
            print dataString
            rrdtool.update(dataFile, dataString)
            time.sleep(300)
        except KeyboardInterrupt:
            print "Exiting..."
            sys.exit()
