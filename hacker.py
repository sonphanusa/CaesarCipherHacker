# EEC 688 Project
# CAESAR CIPHER CHALLENGE
# Fill in your name (id)
#
# Hacker:
# - Prompt for user-input cipher message
# - Hack it to output the key and the plaintext message
#
# Helps:
# http://stackoverflow.com/questions/19338113/how-to-find-possible-english-words-in-long-random-string
#
# Dictionary (UNIX):
# (this is how words.txt created, basically a list of valid words in English)
# cat /usr/share/dict/words > words.txt
#
# Vocab:
# A corpus or text corpus is a large and structured set of texts,
# used for statistical analysis and hypothesis testing,
# checking occurrences or validating linguistic rules
# within a specific language territory. (Wikipedia)

from string import maketrans

# SETUP DICTIONARY and VARIABLES
dictionary  = set(open('words.txt','r').read().lower().split()) #set of words
max_len     = max(map(len, dictionary)) #length of the longest word in the set of words
alphabet    = "what are the alphabets? (abcd...)"

# CAESAR FUNCTIONS
def translator(text, intab, outtab):
    trantab = maketrans(intab, outtab)
    return text.translate(trantab)

def caesar_encode(plaintext, k, letters):
    subs = #fill in your answer for exercise 1 here
    return translator(plaintext, letters, subs)

def caesar_decode(ciphertext, k, letters):
    subs = #fill in your answer for exercise 2 here
    return translator(ciphertext, letters, subs)

# MAIN
print "CAESAR CIPHER CHALLENGE (English)"
print "--- Hacker ---"

print
# GET USER INPUT
cipher_ms = #fill in the blank here for exercise 3

# INIT VARS
words_found = set() #set of words found, starts empty
words_count = []    #list of words count
guess_texts = []    #list of guessed texts

# BRUTE-FORCE CAESAR GUESSING
# Loop from k=1 to k=length-of-alphabet-string (ie. 26) and decode cipher message
# Slice through decoded message as chunks to match words in dictionary
# Count number of words that matched and append the count to a list/array
# whichever k that led to the most words matched has the highest probability of decoding the original text.
print
print "RESULTS"
for k in xrange(len(alphabet)):
    guesstext = #decode cipher message for each k value
    guess_texts.extend([guesstext]) #store into list

    for i in xrange(len(guesstext)):        #for each possible starting position in the corpus
        #chunk that is the size of the longest word
        chunk = guesstext[#fill in here: slice the decoded message from i to length of longest word]

        for j in xrange(1, len(chunk)+1):   #loop to check each possible subchunk
            word = chunk[:j]                #subchunk

            if word in dictionary:          #constant time hash lookup if it's in dictionary
                words_found.add(word)       #add to set of words

    words_count.extend([len(words_found)])  #store number of words found into list
    words_found.clear() #clear set, ready for the next iteration

max_count = max(words_count) #max number of words found
# List of keys sorted descending by the number of words matched in dictionary
key_list  = sorted(range(len(words_count)), key=lambda k:words_count[k], reverse=True)

for i in xrange(len(key_list)):
    # Calculate the probability of each guess by dividing the number of words count
    # of each k to the highest number of words found
    guessprob = "({0:.1f}%)".format(#fill in the equation here)
    print "k =", key_list[i], "-> message:", guess_texts[key_list[i]], guessprob