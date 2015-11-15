sysp = 0
savedc = 0
var = raw_input ("RUN>")

def dispcmd(lines):
    if lines == """]
""":
        sysp = "null"
    else:
        if lines not in ('''display [
''', ''']
''', '''wait ['''):
            print lines[:-1]
            sysp = "txtp"
def waitcmd(lines):
    import time
    if lines == """]
""":
        pass
    if lines not in ('''wait [
''', ''']
'''):
        try:
            time.sleep(lines)
        except:
            print "TIME NOT VALID"
        else:
            pass
        

        
with open(var) as openfileobject:
    for line in openfileobject:
        if line == """display [
""":
            dispcmd("")
        if line == """wait [
""":
            waitcmd('')
        if line == line:
            dispcmd(line)




