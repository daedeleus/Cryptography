import sys
'''
Common functions
'''
def call(func,plaintext,key=""):
    global enc_type
    return func(plaintext,key)


def shift_sub(a,n): #out of bounds check
    ch = chr(ord(a)+n)
    if (a.isupper() and ord(ch)>90) or (a.islower() and ord(ch)>122):
        ch = chr(ord(ch)-26)
    elif (a.isupper() and ord(ch)<65) or (a.islower() and ord(ch)<97):
        ch = chr(ord(ch)+26)
    if not ch.isalpha():
        ch = shift_sub(a,0)
    return ch 

'''
rot13 - circularly shifts alphabets by 13
'''
def rot13(plaintext,*args): # substitution ciphertext with n=13 rotation
    ciphertext = ""
    for a in plaintext:
        if (a.isalpha()):
            ciphertext += shift_sub(a,13)
        else:
            ciphertext += a
    return ciphertext

'''
sse - succesively changes the shift amount by 1
'''
def sse(plaintext,*args): # succesive shift encoder
    ciphertext = ""
    i = 0
    for a in plaintext:
        if (a.isalpha()): 
            ciphertext += shift_sub(a,i)
            i += 1 # shift amount
        else:
            ciphertext += a
    return ciphertext

def sse_d(ciphertext,*args): # succesive shift decoder 
    plaintext = ""
    i = 0
    for a in ciphertext:
        if (a.isalpha()): 
            plaintext += shift_sub(a,-i)
            i += 1
        else:
            plaintext += a
    return plaintext

'''
vignere - uses a lookup table and a key 
'''

def vignere(plaintext,key): # encrypted using a look up table
    ciphertext = ""
    rkey = key 
    if(len(key)<len(plaintext)): #key repetition
        rkey = key*(len(plaintext)//len(key))

    i = 0
    for a in plaintext:
        if (a.isalpha()):
            k = rkey[i]
            i+=1
            ciphertext += shift_sub(a,ord(k)- (65 if k.isupper() else 97))
        else:
            ciphertext += a
    return ciphertext

def vignere_d(ciphertext,key): # decrypted using a look up table
    plaintext = ""
    rkey = key 
    if(len(key)<len(ciphertext)):
        rkey = key*(len(ciphertext)//len(key))

    i = 0
    for a in ciphertext:
        if (a.isalpha()):
            k = rkey[i]
            i+=1
            plaintext += shift_sub(a,-(ord(k)- (65 if k.isupper() else 97)))
        else:
            plaintext += a
    return plaintext
'''
entry point
'''
if __name__ == "__main__":
    if (len(sys.argv)>1):
        plaintext = sys.argv[1] 
        key = sys.argv[2] if len(sys.argv)>2 else 'abc'
        ciphertext = call(vignere,plaintext,key) 
        recovered = call(vignere_d,ciphertext,key)
        print("Ciphertext :\n", ciphertext ,'\n\nRecovered :\n', recovered)
    else:
        print('Give input block at cmd line')
