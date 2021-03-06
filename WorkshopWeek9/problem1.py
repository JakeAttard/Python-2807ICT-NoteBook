def printCommand(vars, val):
    if val.isalpha():
        if val in vars:
            print(val, 'equals', vars[val])
        else:
            print(val, 'is undefined.')
    elif val.isdigit():
        print(val)
    else:
        print("Syntax error.")

def inputCommand(vars, var):
    if not var.isalpha():
        print("Syntax error.")
    else:
        inp = input("Enter a  value  for " +  var +  ": ").strip()
        if inp.isdigit():
            vars[var] = int(inp)
        else:
            print("Syntax error.")

def getsCommand(vars, var, val):
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

def addsCommand(vars, var, val):
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
        printCommand(vars, cs[1])
    elif len(cs) == 2 and cs[0] == 'input':
        inputCommand(vars, cs[1])
    elif len(cs) == 3 and cs[1] == 'gets':
        getsCommand(vars, cs[0], cs[2])
    elif len(cs) == 3 and cs[1] == 'adds':
        addsCommand(vars, cs[0], cs[2])
    else:
        print("Syntax error.")
    command = input("??? ")
print("Goodbye.")