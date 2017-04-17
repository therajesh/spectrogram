#HW7 - Parser
#Author - Rajesh Narayan

import sys
import argparse

input_file = None

""" Takes the grammar and the sentence input from the user."""
def fileInput():
	global input_file 
#	input_file = open("grammar1", 'r')
	input_sentence = sys.argv[1]
	print (input_sentence)

#input_sentence = sys.argv[1]
#print (input_sentence)

def main():
	fileInput()

if __name__ == 	"__main__": 
	main()