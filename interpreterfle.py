sysp = 0
savedc = 0
var = raw_input ("RUN>")

def dispcmd(lines):
    if lines == """]
""":
        sysp = "null"
    else:
        if lines != """display [
""":
            print lines[:-2]
            sysp = "txtp"

        
with open(var) as openfileobject:
    for line in openfileobject:
        if line == """display [
""":
            dispcmd("")
        if line == line:
            dispcmd(line)




