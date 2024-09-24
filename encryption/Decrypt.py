def decrypt(string, shift):
    cipher = ""
    for char in string:
        if char == " ":  # Keep spaces as they are
            cipher += char
        elif char.isupper():  # Decrypt uppercase letters
            cipher += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():  # Decrypt lowercase letters
            cipher += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isdigit():  # Decrypt digits
            cipher += chr((ord(char) - shift - 48) % 10 + 48)
        elif char in "()[]{}":  # Decrypt brackets
            brackets = "()[]{}"
            idx = brackets.index(char)
            cipher += brackets[(idx - shift) % len(brackets)]
        else:  # Keep other characters unchanged
            cipher += char
    return cipher


# Input and execution
text = input("Enter the string to decrypt: ")
s = int(input("Enter shift number: "))
print("Original string: ", text)
print("After decryption: ", decrypt(text, s))
