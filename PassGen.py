import random
import string

while True:
#Enter username
    user = input("Please enter a username: ")


#Length of username
    userlength = len(user)
    print("* Length of username:", userlength)
    
#Alpha-numeric check
    alphanum = user.isalnum()
    print("* All characters are alpha-numeric:", alphanum)
    
#First and last characters are numbers
#
#
#I use "and" in the "if" statement because the demo code on the assignment is wrong
#
#
    firstlet = user[0]
    lastlet = user[-1]
    if (firstlet.isnumeric() is True) and (lastlet.isnumeric() is True):
        print("* First & last characters are not digits: False")
    else:
        print("* First & last characters are not digits: True")

#Checking and printing how many upper and lower case letters
    lower=0
    upper=0
    for i in user:
          if(i.islower()):
                lower=lower+1
          elif(i.isupper()):
                upper=upper+1
    print("* # of uppercase characters in the username:", upper)
    print("* # of lowercase characters in the username:", lower)
            
#Quantity of digits are in string
    numbers = sum(dig.isdigit() for dig in user)    
    print("* # of digits in the username:", numbers)

#If statements when user is invalid
    if (userlength > 15 or userlength < 8) or (alphanum == False) or ((firstlet.isnumeric() is True) or (lastlet.isnumeric() is True)) or (upper <= 1 or lower <= 1) or (numbers <= 1):
        print("Username is invalid, please try again")
        print('')
    else:
        print("Username is valid!")
        break
print('')









#Begin Password
while True:
#Password input
    password = input("Enter a Password: ")

#Password length
    len_pass = len(password)
    print("* Length of password: ", len_pass)

#If username is part of password
    name = 0
    if user in password:
        name += 1
        print ('* Username is part of password: True')
    else:
        name == 0
        print ('* Username is part of password: False')
        
#Amount of uppercase letters
    num_up = 0
    for i in password:
        if i.isupper() == True:
            num_up += 1
    print("* # of uppercase characters in the password:", num_up)
    
#Amount of lowercase letter
    num_low = 0
    for i in password:
        if i.islower() == True:
            num_low += 1
    print("* # of lowercase characters in the password:", num_low)
    
#Number of digits in password
    num_digit = sum(i.isdigit() for i in password)
    print("* # of digits in the password:", num_digit)

#Special characters
    sp_char = 0
    for i in password:
        if i == "#" or i == "$" or i == "%" or i == "&":
            sp_char+=1
    print("* # of special characters in the password:", sp_char)


#Final if statement
    if len_pass > 8 and name == 0 and num_up > 0 and num_low > 0 and num_digit > 0 and sp_char > 0:
        print("Password is valid!")
        break
    else:
        print("Password is invalid, please try again")
        print()
        question = input("Would you like us to fix your password for you? ")
       # flag = False
        if question == "yes" or question == "Yes" or question == "y":   
            index = random.randint(0,(len(password)-1))
            new_password = password[:index] + "1" + password[index:]
            index = random.randint(0,(len(password)-1))
            new_password = new_password[:index] + "3" + new_password[index:]
            index = random.randint(0,(len(password)-1))
            new_password = new_password[:index] + "7" + new_password[index:]
            index = random.randint(0,(len(password)-1))
            new_password = new_password[:index] + "4" + new_password[index:]
            new_password2=new_password
            new_password2= new_password[:index] + "#" + new_password[index:]
            index = random.randint(0,(len(password)-1))
            new_password2 = new_password2[:index] + "$" + new_password2[index:]
            index = random.randint(0,(len(password)-1))
            new_password2 = new_password2[:index] + "%" + new_password2[index:]
            index = random.randint(0,(len(password)-1))
            new_password2 = new_password2[:index] + "&" + new_password2[index:]
            new_password3=new_password2
            new_password3 = new_password2[:index] + "A" + new_password2[index:]
            index = random.randint(0,(len(password)-1))
            new_password3 = new_password3[:index] + "G" + new_password3[index:]
            index = random.randint(0,(len(password)-1))
            new_password3 = new_password3[:index] + "Y" + new_password3[index:]
            index = random.randint(0,(len(password)-1))
            new_password3 = new_password3[:index] + "F" + new_password3[index:]
            if (password.isnumeric() == False) and (password.upper() == False):
                print("* Adding a random special character at a random position:", password[:4] + new_password[:8])
                print("* Adding a random uppercase character at a random position:", password[:4] + new_password3[:8])
                print("* Adding a random digit character at a random position:", password[:4] + new_password2[:8])
            if (password.isnumeric() == True) and (password.upper() == False):
                print("* Adding a random special character at a random position:", password[:4] + new_password[:8])
                print("* Adding a random uppercase character at a random position:", password[:4] + new_password3[:8])
            if (password.isnumeric() == True) and (password.upper() == True):
                print("* Adding a random special character at a random position:", password[:4] + new_password[:8])
            if (password.isnumeric() == False) and (password.upper() == True):
                print("* Adding a random digit character at a random position:", password[:4] + new_password2[:8])
            if password.isalnum() == True:
                print("* Adding a random special character at a random position:", password[:4] + new_password3[:8])
            print("Your new password is", password[:4] + new_password3[:8])
            break

