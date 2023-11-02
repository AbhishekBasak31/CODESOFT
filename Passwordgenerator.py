import random
import string
import os
#Generates random alphabets in a given length
def foralphabet(lett, upper,lower):
        alphabet=""
        upper_letters = string.ascii_uppercase
        lower_letters = string.ascii_lowercase
        up_alphabet=""
        low_alphabet=""

        #To add random upper case letters in a given length. 
        for _ in range(0,upper):
            up_alpha = random.randrange(0, len(upper_letters))
            up_let = upper_letters[up_alpha]
            up_alphabet = up_alphabet + up_let
        alphabet=alphabet+up_alphabet

        #To add random lower case letters in a given length.       
        for _ in range(0,lower):
            low_alpha = random.randrange(0, len(lower_letters))
            low_let = lower_letters[low_alpha]
            low_alphabet = low_alphabet + low_let
        alphabet=alphabet+low_alphabet
           
        return alphabet
    
#Generate random symbols in a given length    
def forsymbol(symb):
        special_char = ""
        symbols = string.punctuation
        for char in range(0, symb):
            char = random.randrange(0, 11)
            new_2 = symbols[char]
            special_char = special_char + new_2
        return special_char
    
 # Generate random numbers in a given length   
def fornumber(numb):
        number = ""
        numbers = string.digits
        for num in range(0, numb):
            num = random.randrange(0, 10)
            new_3 = numbers[num]
            number = number + new_3
        return number 
    
#for the easy level passsword
def easypassword(letters,symbols,numbers):
        return letters+symbols+numbers
    
#for the hard level password   
def hardpassword(letters,symbols,numbers):
        format =letters+symbols+numbers  
        py_password = "".join(random.sample(format, len(format)))
        return py_password


is_process_complt = False

while(not is_process_complt):  
        os.system("cls")
        print("\nWelcome to the Password Generator 🔒")       
        #Total no.of letters need in  the password 
        nr_letters = int(input("\nHow many letters would you like to add in your password?\n"))
       
        #No.of upper class letter need in the password
        up_letters = int(input(f"\nYou can add total {nr_letters} letters in your password among them how many upper case letters you like to add in your password?\n"))
        
        #Check the  up_letters is under the range of nr_letters or not.
        if up_letters<=nr_letters:
            #No.of lower class letter need in the password
            low_letters = int(input(f"\nYou can add {nr_letters-up_letters} lower case letters in your password?\n"))
            #Check the low_letters is under the remaining range or not.
            if low_letters>nr_letters-up_letters:
                print("Invalid input")
                break
        else:
            print("Invalid input.")
            break
        letter=foralphabet(nr_letters,up_letters,low_letters)
         
         #No.of symbols need in the password
        nr_symbols = int(input("\nHow many symbols would you like to add in your password?\n"))
        symbol=forsymbol(nr_symbols)
         
         #No.of digits need in the password
        nr_numbers = int(input("How many numbers would you like to add in your password?\n"))
        number =fornumber(nr_numbers)
        
        letter=foralphabet(nr_letters,up_letters,low_letters)
        symbol=forsymbol(nr_symbols)
        number =fornumber(nr_numbers)
        
        #Enter the complexity level of the password
        level= input("What would you like to generate(hard/easy)password: ")
        
        #Check the complexity level of the password and execute the associated code with that level
        if level=="easy":
           print(f"\nYour password is : {easypassword(letter,symbol,number)}\n")
        elif level =="hard":
            print(f"\nYour password is :{hardpassword(letter,symbol,number)}\n")       
        else:
            print("Enter a valid choice.")   
             
        #Taking an user input to check weather we should continue the process or not.
        choice=input("Would you like to continue(yes/no) : ") 
        if choice=='no':
            is_process_complt=True  
        elif choice!='yes' and choice!='no':
            print("Invalid choice")
            break                  