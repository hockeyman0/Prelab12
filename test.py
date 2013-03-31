#! /usr/bin/env python

import Processor
import sys
import os
import re

argv = len(sys.argv)

if argv != 2:
	print "Usage: test.py <assembly file>"
	sys.exit(1)

argo = sys.argv[1]


pro32 = Processor.Processor()
assembler = Processor.Assembler.Assembler(argo)

pro32.loadAssemblyFile(assembler)
pro32.simulate()

pro32.outputState()