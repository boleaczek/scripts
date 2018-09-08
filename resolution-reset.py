#!/usr/bin/env python3

import os
import sys

currentRes = os.popen('xrandr | grep "\*" | cut -d" " -f4').read()
os.system(sys.argv[1])
os.system(f"xrandr -s {currentRes}")