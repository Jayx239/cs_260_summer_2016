import sys
if __name__ == '__main__':
	import main
import inspect

def is_palindrome(inputWord):
        startIndex = 0
        endIndex = len(inputWord)-1
        while startIndex < endIndex:
                if inputWord[startIndex] != inputWord[endIndex]:
                        return False
                startIndex = startIndex+1
                endIndex = endIndex - 1

        return True

