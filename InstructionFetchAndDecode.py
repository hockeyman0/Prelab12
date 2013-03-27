#! /usr/bin/env python2.6
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$
#


#comment out the line below if you are wanting to run this as a standalone file
import Memory


class Instruction():
    def __init__(self,op,reg,mem1,mem2):
        self.op = op
        self.reg = reg
        self.mem1 = mem1
        self.mem2 = mem2
    
    def getOp(self):
        return self.op
    
    def getReg(self):
        return self.reg

    def getMem1(self):
        return self.mem1

    def getMem2(self):
        return self.mem2

class InstructionFetchAndDecode():
    def __init__(self, mem):
        self.mem = mem
        self.counter = 0
        
    def updatePC(self, pc):
        self.counter = pc

    def incrementPC(self):
        self.counter = self.counter + 1

    def fetchInstruction(self):
        instruct = self.mem.loadValue(self.counter)
        return instruct

    def processInstruction(self, machineCode):
        

        #get the raw binary instructions:
#put halt into a variable
        halt = getPartialValue(30,31, machineCode)

        #put the three values in op
        op = getPartialValue(27,29, machineCode)

        #get the register value
        reg = getPartialValue(24,26, machineCode)

        #get mem1 op
        mem1Op = getPartialValue(22,23, machineCode)
        #get mem1
        mem1 = getPartialValue(12,21, machineCode)
        
        #get mem2 op
        mem2Op = getPartialValue(10,11, machineCode)
        #get mem2
        mem2 = getPartialValue(0,9, machineCode)

        if (mem1Op == 0):
            mem1Tup = ("reg",mem1)
        elif (mem1Op == 1):
            mem1Tup = ("imm",mem1)
        elif (mem1Op == 2):
            mem1Tup = ("mem",mem1)
        else:
            raise ValueError("Bad memory code, expects description to be 0,1,2")
        
        if(mem2Op == 0):
            mem2Tup = ("reg",mem2)
        elif (mem2Op == 1):
            mem2Tup = ("imm",mem2)
        elif (mem2Op == 2):
            mem2Tup = ("mem",mem2)
        else:
            raise ValueError("Bad memory code, expects description to be 0,1,2")

        if(op == 0):
            opCode = "lw"
        if(op == 1):
            opCode = "sw"
        if(op == 2):
            opCode = "add"
        if(op == 3):
            opCode = "sub"
        if(op == 4):
            opCode = "mul"
        if(op == 5):
            opCode = "div"
        if(op == 6):
            opCode = "beq"
        if(op == 7):
            opCode = "jmp"

        if(halt == 3):
            opCode = "halt"
            mem1Tup = ()
            mem2Tup = ()
            reg = 0

        return Instruction(opCode,reg,mem1Tup,mem2Tup)
        

def getPartialValue(index1,index2,num):
    mask = 0
    ran = range(0,index2 + 1)
    for number in ran:
        mask = mask + (pow(2,number))
    new = num & mask
    ran = range(0,index1+1)
    bit = new>>index1
    return bit
