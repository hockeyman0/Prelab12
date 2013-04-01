#! /usr/bin/env python2.6
#
# $Author: ee364b11 $
# $Date: 2013-03-26 16:48:33 -0400 (Tue, 26 Mar 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364b11/Lab11/Assembler.py $
# $Revision: 54835 $

import sys
import os
import re
import math

class Assembler:
    def __init__(self, filename):
        try:
            infile=open(filename,"r")
        except IOError:
            print 'Error: Unable to open assembly file: %s' %(IOError)
            sys.exit(2)
        self.file=infile
    
    def parseInstruction(self, instructionString):
        opcode={'lw':'000','sw':'001','add':'010','sub':'011','mul':'100','div':'101','beq':'110','jmp':'111'}
        regcode={'$t7':'111','$t6':'110','$t5':'101','$t4':'100','$t3':'011','$t2':'010','$t1':'001','$t0':'000'}
        
        reg=r"\$t"
        reg2=r"!(?P<num>[0-9]+)"
        
        if instructionString=='halt':
            return pow(2,31)+pow(2,30)
        stringBin='00'
        instr=instructionString.split()
        instr2=instr[1].split(',')
        
                
        stringBin+=opcode.get(instr[0])
                
        print stringBin
        
        if instr[0] != 'jmp':
            stringBin+=regcode.get(instr2[0])
        else:
            ob=re.match(reg2, instr2[0])
<<<<<<< .mine
            stringBin+='00001'+self.binConversion(int(ob.group('num')))
            stringBin+='000000000000'
            return self.strToBin(stringBin)
=======
            stringBin+='00001'+self.binConversion(int(ob.group('num')))
            stringBin+='000000000000'
            return self.strToBin(stringBin)
>>>>>>> .r13
        
        if re.match(reg,instr2[1]):
            stringBin+='00'+'0000000'+regcode.get(instr2[1])
        else:
            ob = re.match(reg2, instr2[1])
            if ob:
                stringBin+='01'+self.binConversion(int(ob.group('num')))
            else:
                stringBin+='10'+self.binConversion(int(instr2[1]))
        
        if len(instr2) == 3:
            if re.match(reg,instr2[2]):
                stringBin+='00'+'0000000'+regcode.get(instr2[2])
            else:
                ob = re.match(reg2, instr2[2])
                if ob:
                    stringBin+='01'+self.binConversion(int(ob.group('num')))
                else:
                    stringBin+='10'+self.binConversion(int(instr2[2]))
        else:
            stringBin+='000000000000'
        
        
        return self.strToBin(stringBin)
    
    def strToBin(self,str):
        bin=0
        for i in str:
            bin=bin*2+int(i)
        return bin
    
    
    def binConversion(self, num):
        i = 9
        bin = ''
        for j in range(i+1):
            if 2**i <= num:
                bin+='1'
                num=num-2**i
            else:
                bin+='0'
            i-=1
        return bin
    
    
    
    def loadMemory(self, memory):
        
        lineNum=0
        for line in self.file:
            machine = self.parseInstruction(line)
            memory.storeValue(lineNum, machine)
            lineNum+=1


