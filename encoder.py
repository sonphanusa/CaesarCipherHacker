# EEC 688 Project
# CAESAR CIPHER CHALLENGE
# Fill in your name (id)
#
# Encoder:
# - Prompt for user-input message and key (k value)
# - Encode it and output the cipher text

from string import maketrans

# SETUP VARIABLES
alphabet = "what are the alphabets? (abcd...)"

# CAESAR FUNCTIONS
def translator(text, intab, outtab):
    # see tutorial for maketrans() function here: http://www.tutorialspoint.com/python/string_maketrans.htm
    trantab = maketrans(intab, outtab)
    return text.translate(trantab)

def caesar_encode(plaintext, k, letters):
    subs = #fill in the blank here for exercise 1
    #see *hints* in lab note and this also helps: http://www.diveintopython.net/native_data_types/lists.html
    return translator(plaintext, letters, subs)

# MAIN
print "CAESAR CIPHER CHALLENGE (English)"
print "--- Encoder ---"

print
# GET USER INPUT
input_ms    = #fill in the blank here for exercise 1
input_key   = #fill in the blank here for exercise 1
# ENCODE
#correct this function call below for exercise 1
cipher_ms   = #caesar_encode(input ms variable, input key variable, alphabet variable)
# OUTPUT
print
print "RESULTS"
print "Plaintext:", input_ms
print "Ciphertext:", cipher_ms
print
print