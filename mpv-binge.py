import helpers
import os
import sys

expectedSpecialParams = {'t','c'}
expectedParams = {'o'}
foundSpecial = helpers.getMarkedParams(sys.argv, expectedSpecialParams)
found = helpers.getParams(sys.argv, expectedParams)

dirName = sys.argv[1]
episodes = os.listdir(dirName)

howMany = len(episodes)
if 'c' in foundSpecial:
    howMany = int(foundSpecial['c'])

startTime = '0:00'
if 't' in foundSpecial:
    startTime = foundSpecial['t']

show = '> /dev/null'
if 'o' in found:
    show = ''

for episode_number in range(0,howMany):
    print("Now playing")
    print(episodes[episode_number])
    os.system(f"mpv --start={startTime} '{episodes[episode_number]}'{show}")