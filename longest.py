
print("Accept a list of words and return length of the longest word")

# function to find the longest length in the list
def longestLength(words):
	res=max(words,key=len)
	print("The word with the longest length is:", res,
		" and length is ", len(res))


# Driver Program
a = ["one", "two", "third", "four"]
longestLength(a)
#this code contributed by tvsk
