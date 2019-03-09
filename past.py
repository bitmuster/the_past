#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# This file is licensed under the License GPL-3.0-or-later

# int(time.time())-360*(24-4)*3600 = 1552172121
# git add past.py
# git commit --date 1552172121 -m"message from the past"

import subprocess

filename = 'output.fortune'

with open(filename, 'a') as myfile:

    with subprocess.Popen(["fortune"], stdout=subprocess.PIPE) as proc:
        output = proc.stdout.read()
        myfile.write(output.decode('ascii'))

