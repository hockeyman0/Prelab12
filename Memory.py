#! /usr/bin/env python2.6
#
#$Author: ee364b08 $
#$Date: 2013-03-26 16:33:23 -0400 (Tue, 26 Mar 2013) $
#$Revision: 54833 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364b08/Lab11/Memory.py $

class Memory:
	def __init__(self, size):
		self.memarray = []
		for i in range(size):
			self.memarray.append(0)
	def loadValue(self, location):
		if location < 0 or location > len(self.memarray) - 1:
			raise ValueError('Index out of bounds.')
		else:		
			return self.memarray[location]

	def storeValue(self, location, value):
		if location < 0 or location > len(self.memarray) - 1:
			raise ValueError('Index out of bounds.')
		else:		
			self.memarray[location] = value
	
	def dumpMemory(self):
		for i in range(len(self.memarray)):
			hexstr = hex(i)
			hexstr = hexstr[2:].zfill(4)
			binstr = bin(self.memarray[i])
			binstr = binstr[2:].zfill(32)
			print "{0} -> {1}".format(hexstr, binstr)

class DataMemory(Memory):
	def __init__(self,size):
		Memory.__init__(self, size)

	def dumpMemory(self):
		for i in range(len(self.memarray)):
			hexstr = hex(i)
			hexstr = hexstr[2:].zfill(4)
			print "{0} -> {1}".format(hexstr, self.memarray[i])

class InstructionMemory(Memory):
	def __init__(self,size):
		Memory.__init__(self, size)
		self.numaccess = []
		for i in range(size):
			self.numaccess.append(0)

	def dumpMemory(self):
		for i in range(len(self.memarray)):
			binstr = bin(self.memarray[i])
			binstr = binstr[2:].zfill(32)
			hexstr = hex(i)
			hexstr = hexstr[2:].zfill(4)
			print "{0} -> {1} <{2}>".format(hexstr, binstr, self.numaccess[i])	
		
	def loadValue(self, location):
		if location < 0 or location > len(self.memarray) - 1:
			raise ValueError('Index out of bounds.')
		else:
			self.numaccess[location] += 1
			return self.memarray[location]
class RegisterArray(Memory):
	def __init__(self,size):
		Memory.__init__(self, size)

	def dumpMemory(self):
		for i in range(len(self.memarray)):
			print "$t{0} -> {1}".format(i, self.memarray[i])
		
