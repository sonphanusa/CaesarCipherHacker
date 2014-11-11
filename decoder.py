# EEC 688 Project
# CAESAR CIPHER CHALLENGE
# SON PHAN (2367854)
#
# Decoder: 
# - Prompt for cipher text and key (k value)
# - Decode it and output the plain message  
#
# Help:
# http://www.stealthcopter.com/blog/2009/12/python-cryptograph-using-maketrans-for-substitution-and-full-ciphers/
# http://www.diveintopython.net/native_data_types/lists.html


from string import maketrans

# SETUP VARIABLES
alphabet = "abcdefghijklmnopqrstuvwxyz"
again_ms = ""

# CAESAR FUNCTIONS
def translator(text, intab, outtab):
    trantab = maketrans(intab, outtab)
    return text.translate(trantab)

def caesar_encode(plaintext, k, letters):
    subs = letters[k:]+letters[:k]      #substituted letters
    return translator(plaintext, letters, subs)

def caesar_decode(ciphertext, k, letters):
    subs = letters[-k:]+letters[:-k]    #substituted letters
    return translator(ciphertext, letters, subs)

# MAIN
print "CAESAR CIPHER CHALLENGE (English)"
print "--- Decoder ---"

while (again_ms != "y"):
    print 
    # GET USER INPUT   
    cipher_ms   = raw_input("Input your cipher (ignore case & non-alphabet chars): ").lower()
    input_key   = int(raw_input("Shifted how many letters (key)? k = "))
    # DECODE
    plain_ms   = caesar_decode(cipher_ms, input_key, alphabet)    
    # OUTPUT
    print
    print "RESULTS"
    print "Ciphertext:", cipher_ms
    print "Plaintext:", plain_ms
    print
    print
    # EXIT?   
    again_ms    = raw_input("Exit? ('y' to exit) ").lower()
