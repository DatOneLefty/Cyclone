def dispcmd():
    savedc = ""
    while True:
        codeline = raw_input ("txt>>>")
        if codeline == "]":
            print savedc
            break
        else:
            savedc = savedc + codeline
