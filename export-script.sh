rrdtool xport -s now-1h -e now --step 300 \
DEF:a=environment.rrd:cpuTemp:AVERAGE \
DEF:b=environment.rrd:boardTemp:AVERAGE \
DEF:c=environment.rrd:calibTemp:AVERAGE \
DEF:d=environment.rrd:atm:AVERAGE \
DEF:e=environment.rrd:light:AVERAGE \
XPORT:a:"CPU Temp" \
XPORT:b:"Board Temp" \
XPORT:c:"Calibrated Temp" \
XPORT:d:"Atmospheric Pressure" \
XPORT:e:"Light" > stats1h.xml
