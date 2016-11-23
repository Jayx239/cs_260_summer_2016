import palindrome
import sys

print("Welcome to Palindrome Checker!\nEnter a word. The program will tell you if it is a palindrome.\nTo quit enter a blank line.")

sys.stdout.write("Enter word to check: ")
userInput = sys.stdin.readline().replace('\n','').replace('\r','')
while userInput != " " and userInput != "":
	#print(palindrome.is_palindrome(userInput))
	print("The word is a palindrome: " + str(palindrome.is_palindrome(userInput)))
	sys.stdout.write("Enter word to check: ")
	userInput = sys.stdin.readline().replace('\n','').replace('\r','')

