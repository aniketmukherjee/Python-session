#!/usr/bin/env python

import sys

fw = open(sys.argv[2],"wb+")

##"/mnt/python-meetup-2014/simple_text"
content = ''
with open(sys.argv[1],"rb") as fobj:
    for line in fobj:
	fw.write(line)

fw.close()
