"""
Cyclone programming language
by DatOneLefty
"""
print """
    Cyclone Programming language Pre-Alpha Interpreter
    Commit 2
    """
import interpreter as inter
inter.init()
while True:
    codeline = raw_input (">>>")
    inter.run(codeline)
    
