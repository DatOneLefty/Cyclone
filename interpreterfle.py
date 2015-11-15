sysp = 0
savedc = 0
var = raw_input ("RUN>")

def dispcmd(lines):
    if lines == """]
""":
        print savedc
        sysp = "null"
    else:
        savedc = lines
        sysp = "txtp"

        
with open(var) as openfileobject:
    for line in openfileobject:
        if line == """display [
""":
            print "LINEF"
            dispcmd("")
        if line == line:
            print "LINERP"
            dispcmd(line)




