'''
TITLE: Ceasar's Cipher - Explained
DESCRIPTION: What is Caesar's Cipher: 
  - Encrypt: Conceal data by changing it. 
  - Decrypt: Convert the data into its original message. 
  - An encryption and decryption technique. It takes a message and encrypts it by shifting the letters
    in the message by a specific position. To decrypt the message the person needs the encrypted message
    and the specific shift number. 
  For example: If I encrypt the message "hello" and shift the alphabet forward by "5" the output would be "mjqqt". To decode the message
    I need to input "mjqqt" and shift the letters backwards by "5" the output would be "hello"
USED: Defining a function with parameters and arguments, .index(), calling specific values in lists

'''


#Extended list so that there is no out of range error. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#User inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Function that encrypts the text
def encrypt(text_en, shift_en):
  #Empty string that the encrypted message will go in
  cipher_text = ""

  #for loop that looks at the letters in a text then does the following:
  for letter in text:
    #the index() looks for the letter in the list (alphabet) and returns the position of the letter
    position = alphabet.index(letter)
    #Takes the position number and adds the user's shift number
    new_spot = int(shift + position)
    #Looks at the alphabet list at the new position for the new letter
    new_letter = alphabet[new_spot]
    #Adds the new letter to string cipher_text
    cipher_text += new_letter
    
  print(f"The encoded text is: {cipher_text}")   
  
#Function that decrypts the text
def decrypt(text_de, shift_de):
  cipher_text_decode = ""

  #Same idea as the encrypt, except we subtract the shift from the position.
  for letter in text_de:
    position = alphabet.index(letter)
    new_position = int(position - shift)
    new_letter = alphabet[new_position]
    cipher_text_decode += new_letter
  
  print(f"The decoded text is: {cipher_text_decode}")  

#If/Else loop that calls the functions. 
if direction == "encode":
  encrypt(text_en=text, shift_en=shift)
elif direction == "decode":
  decrypt(text_de=text, shift_de=shift)
