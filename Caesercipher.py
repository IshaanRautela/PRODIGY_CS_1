alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
## Encryption Function
def encryption(plain_text,shift):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift)%26
            cipher_text+=alphabet[new_position]
        else: 
            cipher_text+=char
    print(f"Text after Encryption : {cipher_text}")
    ## Decryption Function
def decryption(cipher_text,shift):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift)%26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    print(f"Text after Encryption : {plain_text}")
## Main Function
end=False
while not end :
    choice =input("Type 'cipher' to encrpyt the message,'decipher' to decrypt the message \n")
    text=input("Enter the text :\n")
    shiftkey=int(input("Type the value of key :\n"))
    if choice=="cipher":
        encryption(plain_text=text,shift=shiftkey)
    elif choice=="decipher":    
      decryption(cipher_text=text,shift=shiftkey) 
    exit=input("Enter 'Yes' to continue,'No' to exit\n")
    if(exit=="No"):

        end=True
