#!/usr/bin/env python

s = "GACGATGACGCATCGCGTTTTTGATTTCTGTTTGGAACACGTCCTGACAGCTCTATGCTGTTCCAACCTCTGGCCCCGCCTTTAGAATGGAACATTGACGGATTGTATATGTGGATGGTCAGCTAGTACCCTTCGGCTTGTTGTCCTTTCGATGTGCCTGCGAAGGGCATAGTGTATCGCTCTCCCTAACGATATATGGGTCTATCGTGGGTCGCGGCTGGGAAAGCCCTACTTGACACCAGGAGACGTCTTTATTACTATGGTTCCCATGGGCGCAGGGCGAAACGTGGCGTGCTCACTTATGCCGTCAATTTTTATAGACCGTAGATGAGCACTATTAGTATAATTACACTCAACACAGGTGGACGTTAGCACGTCTCGGAGGCCAGCAGGCTTGGTGGCCCTGGTACCAAAACAATGAACCCCGAATTTCGTGTGGCTATCGATCAAGTCTGATCTATCACCTGAGTACCGGTGGTATTTGCCACTATAGGAAGTGTCGCACCGAGCAATGGATATGAGTCTTCCCATAGACGATCTAGGATACAGCCTCTTTCGCTGTAAAAACTTTCTAGTCAAGTTAATCTCGGCCGTGGCGCGCTCCTATTGAGCCGCTCCTCGCTTTGACGTACGATGCCATTGGGTGGACAGGGACTACTAGATACCTAAGATGGGGCCGAGAGCATAACCGTATCAAGTGCATAACCTGCCTGGTTGAGCTGAGCCAATCTTCCCGACGGGTGTATGATCAGGCTCAACGCAGGGCAGCACGCAAGGGGTTCTTCCGAATTCCAAAGTAGGCACCTACTCGATTTTACTCTCCCAAGGAATGTATGTTATTTTAGACTTATGTTTTTCGCCGATAAATTGAGCAAATACCGAATGGCGTGTTTAAAATCCCGCCGAAGGTGTACAAGAGATTCGGGATAGAATGATTACCGCTGTCTACTAGTCATATCTATGCTTCCAGC"


countA = 0
countC = 0
countG = 0
countT = 0

for letter in s:
	if letter == 'A':
		countA += 1
	elif letter == 'C':
		countC += 1
	elif letter == 'G':
		countG += 1
	elif letter == 'T':
		countT += 1
	else:
		print "Wrong output: this is what you got %s" % letter 

# return A C G T
print "%s %s %s %s" % (countA, countC, countG, countT) 
