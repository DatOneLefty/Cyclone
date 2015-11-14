savedc = ""
sysp = ""
var = raw_input ("RUN>")

def dispcmd(line):
    if line == """]
""":
        print savedc
        sysp = "null"
    else:
        savedc = line
        sysp = "txtp"

        
with open(var) as openfileobject:
    for line in openfileobject:
        if sysp == "txtp":
            dispcmd(line)
        if line == """display [
""":
            dispcmd(line)




