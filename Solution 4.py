e1 = "aaabaaa"
e2 = "mama mia en la pizzeria amam"
e3 = "a"
e4 = "bbdaadbb"
e5 = "lorem ipsum dolor sit amettema tis rolod muspi merol"
def checkMirror(x):

    l = len(x) - 1
    
    i = 0
    while ( x[i]==x[l-i] ) and ( i < l - i ):
        i += 1

    if i >= l-i:
        return True
    else:
        return False
    
# No Tocar
print(checkMirror(e1))
print(checkMirror(e2))
print(checkMirror(e3))
print(checkMirror(e4))
print(checkMirror(e5))