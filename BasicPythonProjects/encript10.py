def encrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) + value))
    return output

def decrypt(text, value, output=""):
   for char in text:
       output = "{}{}".format(output, chr(ord(char) - value))
   return output

i = int(raw_input("Increment value: "))

text = raw_input("Type your text: ")
print("Encrypted text: {}".format(encrypt(text, i)))

text = raw_input("\nType for decrypt: ")
print("Decrypted text: {}".format(decrypt(text, i)))