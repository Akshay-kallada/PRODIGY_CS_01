def caesar_cipher(text, shift, mode):
    """
    Encrypt or decrypt text using Caesar Cipher.
    
    Parameters:
    text (str): The input text to process
    shift (int): The number of positions to shift
    mode (str): 'encrypt' or 'decrypt'
    
    Returns:
    str: The processed text
    """
    result = ""
    
    # Determine the shift direction based on mode
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            # Shift uppercase characters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Shift lowercase characters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave other characters unchanged
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("---------------------")
    
    while True:
        # Get user input
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()
        
        if mode == 'q':
            print("Goodbye!")
            break
        elif mode not in ['e', 'd']:
            print("Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")
            continue
        
        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if not 1 <= shift <= 25:
                raise ValueError
        except ValueError:
            print("Invalid shift value. Please enter a number between 1 and 25.")
            continue
        
        # Determine the mode
        if mode == 'e':
            processed_text = caesar_cipher(text, shift, 'encrypt')
            print(f"Encrypted text: {processed_text}")
        else:
            processed_text = caesar_cipher(text, shift, 'decrypt')
            print(f"Decrypted text: {processed_text}")
        
        print()

if __name__ == "__main__":
    main()