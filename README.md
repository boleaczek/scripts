# Usage

## bulk-execute
Bulk execute specified command.
``./bulk_execute.py <command> <path to .txt with parameters>``

## mpv-binge
Binge videos. Requires mpv Media Player.
``./mpv_binge.py <path to direcotory containing videos>``

### Optional parameters:
* ``-o - show mpv output``
* ``-t <time> - skip to specified time in each video``
* ``-c <n> - play n out of all the videos in the folder``
* ``-s <n> - start with n-th episode(in alphabetical order)``

## cpp-class-scaffolder:
Scaffold .cpp file based on provided .h file.
``./cpp-class-scaffolder <path to .h file> <path to output directory>``

## resolution-reset:
Sets resolution to default after running a command. Helpful for some games on wine that change the resolution.
``./resolution-reset.py <command>``