# -*- coding: utf-8 -*-
#Write a method to replace all spaces in a string with ‘%20’.

word = 'Thanks this helped a lot!'
caract = '%20'
final = ''

for x in word:
	if x != ' ':
		final += x
	else:
		final += caract

print final