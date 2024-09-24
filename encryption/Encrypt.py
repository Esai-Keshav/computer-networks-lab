def encrypt(string, shift):
    cipher = ""
    for char in string:
        if char == " ":  # Keep spaces as they are
            cipher += char
        elif char.isupper():  # Encrypt uppercase letters
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Encrypt lowercase letters
            cipher += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():  # Encrypt digits
            cipher += chr((ord(char) + shift - 48) % 10 + 48)
        elif char in "()[]{}":  # Encrypt brackets
            brackets = "()[]{}"
            idx = brackets.index(char)
            cipher += brackets[(idx + shift) % len(brackets)]
        else:  # Keep other characters unchanged
            cipher += char
    return cipher


# Input and execution
text = input("Enter the string to encrypt: ")
s = int(input("Enter shift number: "))
print("Original string: ", text)
print("After encryption: ", encrypt(text, s))
