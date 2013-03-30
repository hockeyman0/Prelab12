#! /usr/bin/env python2.6
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import sys
import os
import Assembler
import Memory
import InstructionFetchAndDecode
import ExecuteUnit


class Processor:
    def __init__(self):
        self.InstructMem = Memory.InstructionMemory(32)
        self.DataMem = Memory.DataMemory(1024)
        self.Reg = Memory.RegisterArray(8)


    def simulate(self):
        newobj=ExecuteUnit.ExecuteUnit(x,self.DataMem,self.Reg)


    def outputState(self):
        self.Reg.dumpMemory()
        self.InstructMem.dumpMemory()
        self.DataMem.dumpMemory()

    def loadAssemblyFile(self, assembler):
        assembler.loadMemory(self.InstructionMem)
