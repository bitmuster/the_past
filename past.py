#!/usr/bin/python3
# -*- coding: utf-8 -*- 

# This file is licensed under the License GPL-3.0-or-later

import subprocess

filename = 'output.fortune'

with open(filename, 'a') as myfile:

    with subprocess.Popen(["fortune"], stdout=subprocess.PIPE) as proc:
        output = proc.stdout.read()
        myfile.write(output.decode('ascii'))

