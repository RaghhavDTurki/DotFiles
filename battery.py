#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:52:54 2021

@author: raghhav
"""

f = open("/sys/class/power_supply/BAT1/energy_now", "r")
batt_now = int(f.read())
batt_full = 38470000
batt_percent = (batt_now / batt_full) * 100
final_str = "Battery: {}%".format(int(batt_percent))
print(final_str)