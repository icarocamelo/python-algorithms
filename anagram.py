#Write a method to decide if two strings are anagrams or not.
word = 'laval' #nurun


reverse = word[::-1]

print reverse

if word == reverse:
	print 'true'
else:
	print 'false'

