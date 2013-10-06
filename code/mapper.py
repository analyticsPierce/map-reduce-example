#!/usr/bin/env python
# encoding: utf-8
"""
mapper.py

Created by Jason Pierce on 2012-04-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

for line in sys.stdin:
	words = line.split()
	for word in words:
		print word+"\t"+str(1)	
