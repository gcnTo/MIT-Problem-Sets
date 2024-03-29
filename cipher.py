# Problem Set 4B
# Name: gcnTo
# Collaborators: None
# Time Spent: 4-6 hours

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
        

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
            
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
    
        Returns: a dictionary mapping a letter (string) to 
        another letter (string). 
        '''
        if shift > 26:
                shift -= 26
        
        lower_case_dict = {}
            
        for i in range(len(string.ascii_lowercase)):
            #[97,122]
            if (shift + i) > 25:
                lower_case_dict[string.ascii_lowercase[i]] = i+shift-26
            else:
                lower_case_dict[string.ascii_lowercase[i]] = i+shift
           
        for key in lower_case_dict:
            if key in string.ascii_lowercase:
                lower_case_dict[key] = string.ascii_lowercase[lower_case_dict[key]]
                
        upper_case_dict = {}
        
        for i in lower_case_dict:
            upper_case_dict[i.upper()] = lower_case_dict[i].upper()
            
        total_dict = {}
        
        for i in lower_case_dict:
            total_dict[i] = lower_case_dict[i]
            for j in upper_case_dict:
                total_dict[j] = upper_case_dict[j]
        
        return total_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        punctuation_spaces = {}
        
        for i in range(len(self.message_text)):
            if self.message_text[i] not in string.ascii_lowercase:
                punctuation_spaces[i] = self.message_text[i]
        
        
        message_text_new = []
        shift_dict = Message(self.message_text).build_shift_dict(shift)
        
        for i in self.message_text:
            if i in shift_dict:
                message_text_new.append(shift_dict[i])
        new_message_text = "".join(message_text_new)
        
        for key in punctuation_spaces:
            new_message_text = new_message_text[:key] + punctuation_spaces[key] + new_message_text[key:]
        return new_message_text
            

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message(text).build_shift_dict(shift)
        self.message_text_encrypted = Message(text).apply_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        text = self.message_text
        self.shift = shift
        self.encryption_dict = Message(text).build_shift_dict(shift)
        # print(self.message_text_encrypted) 
        self.message_text_encrypted = Message(text).apply_shift(shift)
        # print(self.message_text_encrypted)
    
    # FOR DEBUGGING
    def __str__(self): 
        return "{self.message_text_encrypted}".format(self=self)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        old_counter = 0
        best_key = 0
        for shift_key in range(26):
            decrypted = Message(self.message_text).apply_shift(shift_key + 1)
            decrypted_split = decrypted.split(" ")
            
            new_counter = 0
            for word in decrypted_split:
                if word in self.valid_words:
                    # print(word)
                    new_counter += 1
                    
            if new_counter > old_counter:
                old_counter = new_counter
                best_key = shift_key + 1
            
                
        
        return (best_key, Message(self.message_text).apply_shift(best_key))
    
        

    
            
        
            
        

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 3)
    print('Expected Output: khoor')
    print('Actual Output:', plaintext.get_message_text_encrypted(),"\n")
    
    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('khoor')
    print('Expected Output:', (23, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message(),"\n")
    
    #Example test case story decryption.
    ciphertext = CiphertextMessage(get_story_string().lower())
    print("Encrypted Message:", get_story_string(),"\n") 
    print('Decrypted Message:', ciphertext.decrypt_message())
