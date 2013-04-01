#! /usr/bin/env python2.6
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import sys
import os
import math
import Assembler
import Memory
import InstructionFetchAndDecode
import ExecuteUnit


class Processor:
    def __init__(self):
        self.InstructMem = Memory.InstructionMemory(32)
        self.DataMem = Memory.DataMemory(1024)
        self.Reg = Memory.RegisterArray(8)
        self.FetchDec = InstructionFetchAndDecode.InstructionFetchAndDecode(self.InstructMem)
        self.ExeUnit=ExecuteUnit.ExecuteUnit(self.FetchDec,self.DataMem,self.Reg)

    def simulate(self):
		#halt = pow(2,31) + pow(2,30)
		#temp = 0
		#count = 0
		for loops in range(32):
			self.ExeUnit.executeInstruction()
			
			
		#while (temp != halt) or (count < 31):
		#	machinecode = 
		#pass

    def outputState(self):
        self.Reg.dumpMemory()
        self.InstructMem.dumpMemory()
        self.DataMem.dumpMemory()

    def loadAssemblyFile(self, assembler):
        assembler.loadMemory(self.InstructMem)
