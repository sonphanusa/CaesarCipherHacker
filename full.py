# EEC 688 Project
# CAESAR CIPHER CHALLENGE
# SON PHAN (2367854)
#
# Helps:
# http://www.stealthcopter.com/blog/2009/12/python-cryptograph-using-maketrans-for-substitution-and-caesar-ciphers/
# http://stackoverflow.com/questions/19338113/how-to-find-possible-english-words-in-long-random-string
#
# Dictionary (UNIX):
# cat /usr/share/dict/words > words.txt
#
# Vocab:
# A corpus or text corpus is a large and structured set of texts,
# used for statistical analysis and hypothesis testing, checking occurrences or validating linguistic rules
# within a specific language territory. (Wikipedia)

from string import maketrans

# SETUP DICTIONARY and VARIABLES
dictionary  = set(open('words.txt','r').read().lower().split())
max_len     = max(map(len, dictionary)) #longest word in the set of words
words_found = set() #set of words found, starts empty
words_count = []    #list of words count
guess_texts = []    #list of guessed texts

alphabet    = "abcdefghijklmnopqrstuvwxyz"

# GET USER INPUT
print "CAESAR CIPHER CHALLENGE (English)"
input_ms    = raw_input("Input your message (ignore case & non-alphabet chars): ").lower()
input_key   = int(raw_input("Shift how many letters? k = "))

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

cipher_ms = caesar_encode(input_ms, input_key, alphabet)
decode_ms = caesar_decode(cipher_ms, input_key, alphabet)

print
#print "Plaintext:", input_ms
print "--> CIPHER TEXT:", cipher_ms
print
print "EXPECTED RESULT"
print "Decoded:", decode_ms


# BRUTE-FORCE CAESAR GUESSING
# Loop from k=1 to k=length-of-alphabet-string (ie. 26) and decode cipher message
# Slice through decoded message as chunks to match words in dictionary
# Count number of words that matched and append the count to a list/array
# whichever k that led to the most words matched has the highest probability of decoding the original text.

print #blank line
print "HACKING RESULT"
for k in xrange(len(alphabet)):
    guesstext = caesar_decode(cipher_ms, k, alphabet) #decode cipher message for each k value
    guess_texts.extend([guesstext]) #store into list

    for i in xrange(len(guesstext)):        #for each possible starting position in the corpus
        chunk = guesstext[i : i+max_len+1]  #chunk that is the size of the longest word

        for j in xrange(1, len(chunk)+1):   #loop to check each possible subchunk
            word = chunk[:j]                #subchunk

            if word in dictionary:          #constant time hash lookup if it's in dictionary
                words_found.add(word)       #add to set of words

    words_count.extend([len(words_found)]) #store into list
    words_found.clear() #clear set ready for the next iteration

max_count = max(words_count) #max_index = words_count.index(max_count)
# List of keys sorted descending by the number of words matched in dictionary
key_list  = sorted(range(len(words_count)), key=lambda k:words_count[k], reverse=True)

for i in xrange(len(key_list)):
    # Calculate the probability of each guess by dividing the number of words count
    # of each k to the highest number of words found
    guessprob = "({0:.1f}%)".format((float(words_count[key_list[i]])/max_count)*100)
    print "k =", key_list[i], "-> message:", guess_texts[key_list[i]], guessprob

