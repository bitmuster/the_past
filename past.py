#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# This file is licensed under the License GPL-3.0-or-later

# int(time.time())-360*(24-4)*3600 = 1552172121
# git add past.py
# git commit --date 1552172121 -m"message from the past"

import subprocess
import os

past = 1552172121 + 7

filename = 'output.fortune'

for i in range(300):
    for i in range(10):
        with open(filename, 'a') as myfile:

            for i in range(10):
                with subprocess.Popen(["fortune"], stdout=subprocess.PIPE) as proc:
                    output = proc.stdout.read()
                    myfile.write(output.decode('ascii'))

        os.system('git add *')
        os.system('git commit --date %i -m\"message from the past\"'%past)
        past += 1
    past += 48*3600

print(f'End time of the past is now {past}')

    
