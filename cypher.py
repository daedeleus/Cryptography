import sys
def sub(a,n): #out of bounds check
    ch = chr(ord(a)+n)
    if (a.isupper() and ord(ch)>90) or (a.islower() and ord(ch)>122):
        ch = chr(ord(ch)-26)
    elif (a.isupper() and ord(ch)<65) or (a.islower() and ord(ch)<97):
        ch = chr(ord(ch)+26)
    return ch 

def rot13(message):
    cipher = ""
    for a in message:
        
        if (a.isalpha()): # 78, 110
            cipher += sub(a,13)
        else:
            cipher += a
    return cipher

def sse(message): # succesive shift encoder
    cipher = ""
    for i,a in enumerate(message):
       pass 
    return cipher

if (len(sys.argv)>1):
    message = sys.argv[1] 
    print("Your encrypted text :\n", rot13(message) ,'\nFor :', rot13(rot13(message)))
else:
    print('Give input block at cmd line')
