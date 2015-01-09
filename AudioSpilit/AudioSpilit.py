#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-10-20 15:49:27
# @Last Modified by:   joshua
# @Last Modified time: 2014-10-27 14:16:33

import os
import re
from optparse import OptionParser
from operator import itemgetter
import wavepoint

def get_list_index(List, value):
    return [i for (i, j) in enumerate(List) if j == value]

def get_time_points_from_audio(audioPath, audiolength, step):
    # Get all energy points from audio.
    pointLists = wavepoint.analyze(audioPath)

    # Sort points by energy.
    sortByEnergy = sorted(pointLists, key=itemgetter('energy'))

    # Pick up a few of the minimize point.
    energylists = [x['energy'] for x in sortByEnergy]
    average = sum(energylists) / len(energylists)
    averageLists = [x / average * 100 for x in energylists if x / average * 100 < 1.0]
    timelists = sorted([x['time'] for x in sortByEnergy[:len(averageLists)]])

    aimlists = []
    for x in range(int(audiolength / step)):
        comparelist = [{'time': y, 'abstime': abs(y - (x + 1) * step)} for y in timelists]
        comparelist = sorted(comparelist, key=itemgetter('abstime'))
        aimlists.append(comparelist[0]['time'])
        index = get_list_index(timelists, comparelist[0]['time'])
        timelists = timelists[index[0]:]

    return aimlists

# # Read options
# parser = OptionParser()
# parser.add_option("-i", "--input", dest="input", action="store", help="input x y for each file by user", default="1.wav")
# parser.add_option("-d", "--duration", dest="duration",action="store", help="input spilit duration", default="8")
# (options, args) = parser.parse_args()

# inputfile = '1.wav'
# spilitsize = 8

# if options.input == None or options.input == '':
#     print('Error: no input file, quit')
#     exit()
# else:
#     inputfile = options.input

# if options.duration == None or options.duration == 0:
#     print('Warning: no spilit duration specified, default is 8s')
#     spilitsize = 8

def get_duration(inputfile):
    # Get duration info from input audio file.
    # TODO. think about use python c wavepoint to get duration.
    os.system('mkdir -p tmp; rm -f tmp/out.txt; ffmpeg -i ' + inputfile + ' 2>&1 | grep "Duration" | cut -d " " -f 4 | sed s/,// >> tmp/out.txt')

    with open('tmp/out.txt', 'r') as f:
        durationstr = f.read()
    # print(durationstr)

    # convert duration info to float (s)
    result =  re.findall('(\d+):(\d+):([\d\.]+)', durationstr)
    num = result[0]
    duration = int(num[0]) * 3600 + int(num[1]) * 60 + float(num[2])
    return duration

def do_spilit(inputfile, timespilit):
    # Spilit the audio file
    outdir = inputfile + '.out'
    if os.path.isdir(outdir) == False:
        os.mkdir(outdir)

            # ' -ab ' + bitrate + \
            # ' -ar ' + freq + \
            # ' -ac ' + channels + \
            # ' -acodec ' + codec + \
    for i in range(len(timespilit) - 1):
        cmd = 'ffmpeg -y -i ' + inputfile + \
            ' -ss ' + str(timespilit[i]) + \
            ' -t ' + str(timespilit[i + 1] - timespilit[i]) + ' ' + \
            ' -ab ' + str(16) + ' ' + \
            ' -ar ' + str(16000) + ' ' + \
            outdir + '/' + str(int(timespilit[i] * 1000) / 1000.0) + '-' + str(int(timespilit[i + 1] * 1000) / 1000.0) + '.wav'
        os.system(cmd)

def spilit(inputfile, step):
    duration = get_duration(inputfile)

    # Get aim time points list.
    timespilit = get_time_points_from_audio(inputfile, duration, step)
    timespilit.append(0)
    timespilit.append(duration)
    timespilit = sorted(timespilit)

    do_spilit(inputfile, timespilit)
