# script: AdderR.py
# Adder REPL

def doPrint(vars, val):
    if val.isalpha():
        if val in vars:
            print(val, 'equals', vars[val])
        else:
            print(val, 'is undefined.')
    elif val.isdigit():
        print(val)
    else:
        print("Syntax error.")

def doInput(vars, var):
    if not var.isalpha():
        print("Syntax error.")
    else:
        inp = input("Enter a  value  for " +  var +  ": ").strip()
        if inp.isdigit():
            vars[var] = int(inp)
        else:
            print("Syntax error.")

def doGets(vars, var, val):
    if not var.isalpha():
        print("Syntax error.")
    else:
        if val.isdigit():
            vars[var] = int(val)
        elif val.isalpha():
            if val in vars:
                vars[var] = vars[val]
            else:
                print(val, 'is undefined.')
        else:
            print("Syntax error.")

def doAdds(vars, var, val):
    if not var.isalpha():
        print("Syntax error.")
    else:
        if var not in vars:
            print(var, 'is undefined.')
        else:
            if val.isdigit():
                vars[var] += int(val)
            elif val.isalpha():
                if val in vars:
                    vars[var] += vars[val]
                else:
                    print(val, 'is undefined.')
            else:
                print("Syntax error.")

print("Welcome to the Adder REPL.")
vars = dict()
command = input("??? ").strip()
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
    command = input("??? ")
print("Goodbye.")
