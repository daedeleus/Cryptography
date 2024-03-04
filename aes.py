 
import sys

'''
Common 
'''
kws = []

def call(func,plaintext,key=""):
    return func(plaintext,key)
def lookup(a):
    return a

def g(w):
    nw = ""
    b = list(w)
    t=b[0]
    b[0],b[1],b[2],b[3] = b[1],b[2],b[3],t 
    nwl = [lookup(b[i]) for i in range(0,3)] 
    for i in nwl:
        nw += i
    return nw

def keyword_gen(key,no_rounds):
    global kws
    kw = [key[i:i+4] for i in range(0,4,15)]
    print(kw)
    kws.append(kw)
    print(kws)
    for i in range(no_rounds):
        
        kw[0] = kw[0] ^ g(kw[3])
        kw[1] = kw[1] ^ kw[0]
        kw[2] = kw[2] ^ kw[1]
        kw[3] = kw[3] ^ kw[2]
        kws.append(kw)

'''
aes encode
'''
def substitute(cb): #using look up table
    pass
def shift(cb): 
    '''shifting bytes 
    row 0 - untouched
    row 1 - circular shift -1
    row 2 - circular shift 2
    row 3 - circular shift 1
    '''
    pass
def mix(cb):
    '''
    multiplied with a matrix(4X4)
    '''
    
    pass
def add_key(cb,start):
    '''
    xor operation with key
    '''
    global kws

    return cb ^ kws[start]

def aes(plaintext,key):
    ciphertext = ""
    global kws
    no_blocks = len(plaintext)//16
    blocks = [plaintext[16*i:16*(i+1)] for i in range(no_blocks)]
    no_rounds = 0

    
    if len(key) == 16:
        no_rounds = 10
    elif len(key) == 24:
        no_rounds = 12
    elif len(key) == 32:
        no_rounds = 14
    keyword_gen(key,no_rounds)
    print(len(kws),kws,sep = '\n')
    for cb in blocks:
        
        # round 0
        cb = add_key(cb,0)

        # round 1 to N-1
        for r in range(1,no_rounds):
            cb = substitute(cb)
            cb = shift(cb)
            cb = mix(cb)
            cb = add_key(cb,4*r)
        
        # last round
        cb = substitute(cb)
        cb = shift(cb)
        cb = add_key(cb,4*no_rounds)

        ciphertext += cb
    
    return ciphertext
    
    

'''
aes decode
'''
def aes_d(ciphertext,key):
    pass

'''
entry point
'''

enc_type = aes
dec_type = aes_d 
if __name__ == "__main__":
    if (len(sys.argv)>1):
        plaintext = "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis."
        key = sys.argv[2] if len(sys.argv)>2 else 'abcdefghijklmnop'
        ciphertext = call(enc_type,plaintext,key) 
        recovered = call(dec_type,ciphertext,key)
    else:
        print('Give input block at cmd line')
