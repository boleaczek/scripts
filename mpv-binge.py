#!/usr/bin/env python3

import helpers
import os
import sys

expectedSpecialParams = {'t','c','s'}
expectedParams = {'o'}
foundSpecial = helpers.getMarkedParams(sys.argv, expectedSpecialParams)
found = helpers.getParams(sys.argv, expectedParams)

dirName = sys.argv[1]
episodes = sorted(os.listdir(dirName))

howMany = len(episodes)
if 'c' in foundSpecial:
    howMany = int(foundSpecial['c'])

start = 0
if 's' in foundSpecial:
    start = int(foundSpecial['s'])

startTime = '0:00'
if 't' in foundSpecial:
    startTime = foundSpecial['t']

show = '> /dev/null'
if 'o' in found:
    show = ''

for episode_number in range(start, howMany):
    print("Now playing")
    print(episodes[episode_number])
    os.system(f"mpv --start={startTime} '{episodes[episode_number]}'{show}")