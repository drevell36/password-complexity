# Import getpass function to hide password input
from getpass import getpass

# Set variable string for lower case characters
lower = 'abcdefghijklmnopqrstuvwxyz'
# Set variable string for upper case characters
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Set list string for numbers
numbers = '1234567890'
# Set variable string for special characters
special = "~`!@#$%^&*()\-_=+}{[]|;:',\".<>/?"
# Set empty dictionary to detect repeated characters
duplicates = {}

# Print welcome text
print("This program will check how strong your password is to make sure complexity requirements are met.\nThe password must contain a lower case letter, an uppercase letter, a number and a special character.\nThe minimum length is 8 characters and a maximum of 20 characters.\nThe same character cannot be used more than once and spaces are not allowed.")

# Function to check for repeated duplicate characters
def checkForDuplicates(e):
    for char in password:
        # Checks if char already exists in dictionary
        if char in duplicates:
            duplicates[char] +=1
        else:
            # Sets count to 1 if no duplicates exist
            duplicates[char] =1
    # Checks duplicate characters and count in dictionary
    for result, char in duplicates.items():
        
        if char > 1:
            # Prints message when duplicates are found
            print("Duplicate characters are not allowed. Try again.")
            # Clear dictionary if function is restarted
            duplicates.clear()
            # Returns True value if duplicates are found
            return True
        else:
            # Returns False value if no duplicates are found
            return False

# Function to check characters
def numberOfCharacters():
        # Set variables for counting numbers of characters in password
        l, u, n, s = 0, 0, 0, 0
        # Runs loop on password string
        for i in password:
            # Count how many lower case characters in password
            if(i in lower):
                l +=1
            # Count how many upper case
            if(i in upper):
                u +=1
            # Count how many numbers
            if(i in numbers):
                n +=1
            # Count special characters
            if(i in special):
                s +=1
        # Return counts of lowercase, upper, number, special characters
        return l, u, n, s

# Function to check complexity of password
def checkComplexity():
    # If password contains 4 complexity requirements, print very high
    if(l >0 and u >0 and n >0 and s >0):
        print("Excellent, your password strength is very high, all four complexity requirements were met.")
    # If password contains 3 complexity requirements, print high
    elif(l >0 and u >0 and n >0) or (l >0 and u >0 and s >0) or (u >0 and n >0 and s >0) or (l >0 and n >0 and s >0):
        print("Great, your password strength is high, three complexity requirements were met.")
    # If password contains 2 complexity requirements, print medium
    elif(l >0 and u >0) or (u >0 and n >0) or (l >0 and n >0) or (l >0 and s >0) or (u >0 and s >0) or (n >0 and s >0):
        print("Good, your password strength is medium, two complexity requirements were met.")
    # If password contains 1 complexity requirement, print low
    else:
        print("Whoops, your password strength is low. Only one complexity requirement was met. Please try a more secure password next time.")
    
# Enables program to start again after minimum password length is not met
while True:
    # Prompt user to enter a password and hide the input typed
    password = getpass(prompt= "\nPlease enter your password (Input will be hidden): ")
    # Remove spaces in password
    password = password.replace(" ","")
    password_length = len(password) 
    # Check for duplicate characters in password
    duplicate_status = checkForDuplicates()
    # Restart loop if duplicate characters are detected
    if duplicate_status is True:
        continue
    # Restart program if password is more than 20 characters
    elif(password_length >20):
        print("Password is too long. The maximum is 20 characters.")
        # Restarts the while loop
        continue
    # Check for number of characters is 8 or more
    elif(password_length >=8):
        # Set variables from return values in function
        l, u, n, s = numberOfCharacters()
        # Call function to check complexity
        checkComplexity()
        # Print character length
        print(f"The length of the password was {password_length} characters.\nLowercase: {l} Uppercase: {u} Number: {n} Special: {s}")
    # Restart program if password is less than 8 characters
    else:
        print("Password is too short. A minimum of 8 characters is required.")
        # Restarts the while loop
        continue
    # Breaks while loop and exits program
    break