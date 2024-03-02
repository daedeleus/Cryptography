import sys
def shift_sub(a,n): #out of bounds check
    ch = chr(ord(a)+n)
    if (a.isupper() and ord(ch)>90) or (a.islower() and ord(ch)>122):
        ch = chr(ord(ch)-26)
    elif (a.isupper() and ord(ch)<65) or (a.islower() and ord(ch)<97):
        ch = chr(ord(ch)+26)
    if not ch.isalpha():
        ch = shift_sub(a,0)
    return ch 

def rot13(message):
    cipher = ""
    for a in message:
        if (a.isalpha()): # 78, 110
            cipher += shift_sub(a,13)
        else:
            cipher += a
    return cipher

def sse(message): # succesive shift encoder
    cipher = ""
    i = 0
    for a in message:
        if (a.isalpha()): 
            cipher += shift_sub(a,i)
            i += 1
        else:
            cipher += a
        
    return cipher

if (len(sys.argv)>1):
    message = sys.argv[1] 
    print("Your encrypted text :\n", sse(message) ,'\n\nFor :\n', rot13(rot13(message)), sep='')
else:
    print('Give input block at cmd line')
