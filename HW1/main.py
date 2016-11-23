import palindrome
import sys

def test_palindrome(arguments):
	wordIsPalindrome = False
	passes = 0
	fails = 0
	for argument in arguments:
        	if argument == sys.argv[0]:
                	continue
		wordIsPalindrome  = palindrome.is_palindrome(argument)
		if wordIsPalindrome:
			passes = passes + 1
		else:
			fails = fails + 1
	#print(argument + ": " + str(wordIsPalindrome))
	if fails < 1:
		print("Success! Passed " + str(passes) + "/" + str(passes+fails) + " tests.")
	else:
		print("Fail! Passed " + str(passes) + "/" + str(passes+fails) + " tests.")

#caller_script = inspect.stack()[1][1]
#print(caller_script)
#if caller_script == "palindrome.py":
test_palindrome({"undertakes", "impassibly", "pop", "misericordia", "pup", "dinars", "misprisions", "tot"})
