import sys
import aes

'''
Common functions
'''
def call(func,plaintext,key=""):
    return func(plaintext,key)


'''
entry point
'''
enc_type = aes
dec_type = aes_d
if __name__ == "__main__":
    if (len(sys.argv)>1):
        plaintext = sys.argv[1] 
        key = sys.argv[2] if len(sys.argv)>2 else 'abc'
        ciphertext = call(aes,plaintext,key) 
        recovered = call(aes_d,ciphertext,key)
        print("Ciphertext :\n", ciphertext ,'\n\nRecovered :\n', recovered)
    else:
        print('Give input block at cmd line')
