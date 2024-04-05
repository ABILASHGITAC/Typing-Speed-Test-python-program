# Importing the time module for time-related functions
import time

# Define the phrase that the user needs to type
string = "Python is an interpreted, high-level programming language"

# Count the number of words in the string
word_count = len(string.split())

# Decorative border for visual presentation
border = '-+-'*10

# Function to display decorative border and instructions
def createbox():
    print(border)
    print()
    print('Enter the phrase as fast as possible and with accuracy')
    print()

# Main program loop
while  1:
    # Record the start time before displaying instructions and phrase
    t0 = time.time()
    
    # Display instructions and phrase for the user
    createbox()
    print(string,'\n')
    
    # Prompt the user to type the phrase
    inputText = str(input())
    
    # Record the end time after the user has entered their input
    t1 = time.time()
    
    # Calculate the length of the input text (number of words)
    lengthOfInput = len(inputText.split())
    
    # Calculate the accuracy by finding the intersection of words between the input text and the original phrase
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy/word_count)
    
    # Calculate the time taken to type the input
    timeTaken = (t1 - t0)
    
    # Calculate the typing speed in words per minute
    wordsperminute = (lengthOfInput/timeTaken)*60 
    
    # Showing results now
    print('Total words \t :' ,lengthOfInput)
    print('Time used \t :',round(timeTaken,2),'seconds')
    print('Your accuracy \t :',round(accuracy,3)*100,'%')
    print('Speed is \t :' , round(wordsperminute,2),'words per minute')
    
    # Prompt the user if they want to retry
    print("Do you want to retry",end='')
    
    # If user inputs anything, continue with the loop; otherwise, exit the loop and end the program
    if input():
        continue
    else:
        print('Thank you , bye bye .')
        time.sleep(1.5)  # Wait for 1.5 seconds before exiting
        break
