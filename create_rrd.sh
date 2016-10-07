#!/bin/bash

# 576 5 minute samples: 2 days
# 672 60 minute samples: 28 days

rrdtool create environment.rrd  \
    --start now                 \
    --step 60                   \
    DS:cpuTemp:GAUGE:120:-20:50    \
    DS:boardTemp:GAUGE:120:-20:50    \
    DS:calibTemp:GAUGE:120:-20:50    \
    DS:atm:GAUGE:120:0:U        \
    DS:light:GAUGE:120:0:U      \
    RRA:AVERAGE:0.5:1:60        \
    RRA:AVERAGE:0.5:5:576       \
    RRA:AVERAGE:0.5:60:672
