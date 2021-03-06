#! /usr/bin/env python2.6
#$Author: ee364a14 $
#$Date: 2013-03-26 16:43:56 -0400 (Tue, 26 Mar 2013) $
#$Revision: 54834 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364a14/Lab11/ExecuteUnit.py $

import sys, os, Memory, InstructionFetchAndDecode

class ExecuteUnit:

	def __init__(self,fetchUnit,dataMem,registers):
		self.fetch = fetchUnit
		self.data = dataMem
		self.registers = registers

	def executeInstruction(self):
		machinecode = self.fetch.fetchInstruction()#import machine code here
		InstructionObject = self.fetch.processInstruction(machinecode)
		#instructionOBJ
		op = InstructionObject.getOp()

		if op == 'lw':
			tup1 = InstructionObject.getMem1()
			tup2 = InstructionObject.getMem2()
			if tup1[0] == 'imm':
				valtoload = tup1[1]
			elif tup1[0] == 'reg':
				valtoload = self.registers.loadValue(tup1[1])
			else:
				valtoload = self.data.loadValue(tup1[1])
			
			self.registers.storeValue(tup2[1],valtoload)
			self.fetch.incrementPC()
		elif op == 'sw':
			reg = InstructionObject.getReg()
			valtoload = self.registers.loadValue(reg)
			tup1 = InstructionObject.getMem1()
			self.data.storeValue(tup1[1],valtoload)
		elif op == 'add':
			tup1 = InstructionObject.getMem1()
			tup2 = InstructionObject.getMem2()
			reg = InstructionObject.getReg()

			num1 = self.data.loadValue(tup1[1])
			num2 = self.data.loadValue(tup2[1])

			self.registers.storeValue(reg,num1+num2)
		elif op =='sub':
			tup1 = InstructionObject.getMem1()
			tup2 = InstructionObject.getMem2()
			reg = InstructionObject.getReg()

			num1 = self.data.loadValue(tup1[1])
			num2 = self.data.loadValue(tup2[1])

			self.registers.storeValue(reg,num1-num2)
		elif op == 'mul':
			tup1 = InstructionObject.getMem1()
			tup2 = InstructionObject.getMem2()
			reg = InstructionObject.getReg()

			num1 = self.data.loadValue(tup1[1])
			num2 = self.data.loadValue(tup2[1])

			self.registers.storeValue(reg,num1*num2)
		elif op == 'div':
			tup1 = InstructionObject.getMem1()
			tup2 = InstructionObject.getMem2()
			reg = InstructionObject.getReg()

			num1 = self.data.loadValue(tup1[1])
			num2 = self.data.loadValue(tup2[1])

			self.registers.storeValue(reg,num1/num2)
		elif op == 'beq':
			reg = InstructionObject.getReg()
			tup1 = InstructionObject.getMem1()

			num1 = self.register.loadValue(reg)
			if num1 == 0:
				self.fetch.updatePC(tup1[1])
			else:
				self.fetch.incrementPC()
		elif op == 'jmp':
			tup1 = InstructionObject.getMem1()
			self.fetch.updatePC(tup1[1])

				
