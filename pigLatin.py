
def isVowel(letter):
	if (letter == 'a' or letter == 'A'):
		return True
	elif(letter == 'e' or letter == 'E'):
		return True
	elif(letter == 'i' or letter == 'I'):
		return True
	elif(letter == 'o' or letter == 'O'):
		return True
	elif(letter == 'u' or letter == 'U'):
		return True
	elif(letter == 'y' or letter == 'Y'):
		return True
	else:
		return False;


def convert(word):
	firstLet = word[0]
	seclet = word[1]
	wordSub = word[1:]
	vowel = isVowel(firstLet)
	svowel = isVowel(seclet)
	suffix = "ay"
	nword = str()
	if(vowel):
		suffix = 'w' + suffix
		nword = word + suffix
	elif(svowel):
		nword = wordSub + firstLet + suffix
	else:
		twosub = word[0]+word[1]
		wordSub = wordSub[1:]
		nword = wordSub + twosub + suffix
	return nword


x = input("Enter a word: ")
answer = convert(x)
print(answer)