# EEC 688 Project
# CAESAR CIPHER CHALLENGE
# Fill in your name (id)
#
# Decoder:
# - Prompt for cipher text and key (k value)
# - Decode it and output the plain message

from string import maketrans

# SETUP VARIABLES
alphabet = "what are the alphabets? (abcd...)"

# CAESAR FUNCTIONS
def translator(text, intab, outtab):
    # see tutorial for maketrans() function here: http://www.tutorialspoint.com/python/string_maketrans.htm
    trantab = maketrans(intab, outtab)
    return text.translate(trantab)

def caesar_decode(ciphertext, k, letters):
    subs = #fill in the blank here for exercise 2
    #see *hints* in lab note and this also helps: http://www.diveintopython.net/native_data_types/lists.html
    return translator(ciphertext, letters, subs)

# MAIN
print "CAESAR CIPHER CHALLENGE (English)"
print "--- Decoder ---"

print
# GET USER INPUT
cipher_ms   = #fill in the blank here for exercise 2
input_key   = #fill in the blank here for exercise 2
# DECODE
#correct this function call below for exercise 2
plain_ms   = #caesar_decode(cipher ms variable, input key variable, alphabet variable)
# OUTPUT
print
print "RESULTS"
print "Ciphertext:", cipher_ms
print "Plaintext:", plain_ms
print
print