S1 = 1
S2 = 2
S3 = 3
S4 = 4

state = 1
string = input("The string to be recognised ")

while len(string) > 0:
    c = string[0]
    string = string[1:]
    
    if state == S1:
        if c == '1': state = S2
        if c == '0': state = S3
    elif state == S2:
        if c == '1': state = S4
        if c == '0': state = S3
    elif state == S3:
        if c == '1': state = S2
        if c == '0': state = S4
    else:
        if c == '1': state = S4
        if c == '0': state = S4

if state == S4:
    print("Accepted")
else:
    print("Not accepted")
    
        
