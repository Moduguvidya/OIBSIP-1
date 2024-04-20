import random
import string
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_symbols:
        characters += string.punctuation
    if use_digits:
        characters += string.digits
    if not characters:
        print("Error:please select at least one character type.")
        return None
    password= ''.join(random.choice(characters)for _ in range(length))
    return password
def main():
    print("welcome to the password Generator!")
    length = int(input("Enter the length of the password: "))
    use_uppercase =(input("Include uppercase letters?(yes/no): ")).lower() =='yes'
    use_lowercase =(input("Include lowercase letters?(yes/no): ")).lower() =='yes'
    use_symbols = (input("Include symbols? (yes/no): ")).lower()== 'yes'
    use_digits = (input("Include digits? (yes/no): ")).lower()== 'yes'
    password = generate_password(length,use_uppercase,use_lowercase,use_symbols,use_digits)
    if password:
         print("your generated password is:",password)
if __name__== "__main__":
    main()          
      


       


           
