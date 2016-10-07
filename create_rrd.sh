#!/bin/bash

# 576 5 minute samples: 2 days
# 672 60 minute samples: 28 days

rrdtool create environment.rrd \
    --start now \
    DS:temp:GAUGE:576:-20:50    \
    DS:atm:GAUGE:576:0:U    \
    DS:light:GAUGE:576:0:U    \
    RRA:AVERAGE:0.5:1:576       \
    RRA:AVERAGE:0.5:12:672
