# EEC 688 Project
# CAESAR CIPHER CHALLENGE
# SON PHAN (2367854)
#
# Encoder: 
# - Prompt for user-input message and key (k value)
# - Encode it and output the cipher text   
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
print "--- Encoder ---"

while (again_ms != "y"):
    print 
    # GET USER INPUT   
    input_ms    = raw_input("Input your message (ignore case & non-alphabet chars): ").lower()
    input_key   = int(raw_input("Shift how many letters (key)? k = "))
    # ENCODE
    cipher_ms   = caesar_encode(input_ms, input_key, alphabet)    
    # OUTPUT
    print
    print "RESULTS"
    print "Plaintext:", input_ms
    print "Ciphertext:", cipher_ms
    print
    print
    # EXIT?   
    again_ms    = raw_input("Exit? ('y' to exit) ").lower()
    
