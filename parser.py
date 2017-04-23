# HW7 - Parser
# Author - Rajesh Narayan
# Some inspiration was taken from a github implementation I found online, https://github.com/stensaethf/CKY-Parser/blob/master/parser.py
import sys
import argparse
from node import Node


""" Takes the grammar and the sentence input from the user."""
def fileInput():

    grammar = open("grammar1.txt", 'r')
    input_sentence = sys.argv[1]
    return grammar, input_sentence

"""Takes the grammar in the input form and translates it into a usable form without any loss in utility"""
def grammarRules(grammar):

    with grammar as f:
        rules = f.readlines()

    #Removes '/n' from the end of every list
    rules = list(map(lambda s: s.strip(), rules))

    #Assigns the rules into lists of lists
    rules_length = len(rules)
    grammar_rules = []
    for line in rules :
        linecount = 0
        if (line[0] != "#"):
            rule = line.split("->")
            rule[0] = rule[0].strip()
            rule[1] = rule[1].strip()
            grammar_rules.append(rule)
    return grammar_rules


"""Takes the sentence and the grammar and tells us whether or not the sentence is possible"""
def CYK (grammar, input_sentence):

    # Create the CYK table
    length = len(input_sentence)
    table = [None] * (length)
    for i in range(length):
        table[i] = [None] * (length+1)
        for j in range(length+1):
            table[i][j] = []

    # Create a pointer table
    pointer = [None] * (length)
    for j in range(length):
        pointer[j] = [None] * (length+1)
        for i in range(length+1):
            pointer[j][i] = []

    # Fill the diagonals with the POS of the words
    for j in range(1, length+1):
        for rule in grammar:
            if[input_sentence[j-1]] in grammar[rule]:
                table[j-1][j].append(rule)
                pointer[j-1][j].append(Node(rule, None, None, input_sentence[j-1]))


    # Fill the CYK table
    for i in range (1, length+1):
        for j in range(i-2, -1, -1):
            for k in range(j+1, i):
                for l in range (0, len(grammar)-1):
                    for derivation in grammar[rule]:
                        if len(derivation) == 2:
                            B = derivation[0]
                            C = derivation[1]

                            # If A -> B C and B in table[i][k] and C in table[k][j].
                            if B in table[i][k] and C in table[k][j]:
                                table[i][j].append(rule)

                                for b in pointer[i][k]:
                                    for c in pointer[k][j]:
                                        if b.root == B and c.root == C:
                                            pointer[i][j].append(Node(rule, b, c, None))

    return pointer[0][n]


def main():
    grammar, input_sentence = fileInput()
    grammar_rules = grammarRules(grammar)
    final = CYK(grammar_rules, input_sentence)
    print(final)

main()