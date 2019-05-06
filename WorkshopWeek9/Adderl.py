
#  script:  AdderI.py
#  Adder  interpreter
# only the main program is different to the REPL


script = open(input("Script name: "))
vars = dict()
command = script.readline().strip()
while command != 'quit':
    cs = command.split()
    if len(cs) == 2 and cs[0] == 'print':
        doPrint(vars, cs[1])
    elif len(cs) == 2 and cs[0] == 'input':
        doInput(vars, cs[1])
    elif len(cs) == 3 and cs[1] == 'gets':
        doGets(vars, cs[0], cs[2])
    elif len(cs) == 3 and cs[1] == 'adds':
        doAdds(vars, cs[0], cs[2])
    else:
        print("Syntax error.")
        exit()
    command = script.readline().strip()
script.close()
