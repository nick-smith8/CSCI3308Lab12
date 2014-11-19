# The Computer class is a Facade class which will simplify the computer part classes.
# You should implement this class
# This class should be able to be called by the running part
class Computer:
    
    def __init__(self):
        self.freq="3.5GHz"
        self.coreNum="4"
        self.gen="DDR4"
        self.size="4GB"
        self.fs="NTFS"
        self.volume="1TB"
     
    # implement the class below this line    

    def startComputer(self):
        print "Checking CPU...."
        print "Loading memory..."
        print "Mounting disk..."
        
    def printCPUInfo(self):
        print "CPU info:\n  Frequency: "+self.freq+"\n  Number of cores: "+self.coreNum
        
    def printMemInfo(self):
        print "Memory info:\n  Memory Type: "+self.gen+"\n  Size: "+self.size
        
    def printHDInfo(self):
        print "Hard Disk info:\n  File System: "+self.fs+"\n  Volume: "+self.volume

# The running part
# Don't modify the following code!

com=Computer()
com.startComputer() # When a computer starts, it needs to check the CPU, load the Memory, and then mount the harddisk.
com.printCPUInfo()
com.printMemInfo()
com.printHDInfo()
