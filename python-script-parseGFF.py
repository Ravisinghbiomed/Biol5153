#! /usr/bin/env python3

import argparse

# define the functions

# function to accept command line arguments
def get_args():
	# create an ArgumentParser object
	parser = argparse.ArgumentParser(description='This script parses a GFF file ")
		
# add positional arguments
	parser.add_argument("gff", help="Name of the gff file to prse", type=str)
	parser.add_argument("fasta", help= Name of the FASTA file to prase", type=str)
	
# parse the actual arguments
# acecess argument values via 'args' variable
	args = parser.parse_args()
# open the GFF file
	with open(args.gff)as x:
	
#loop over all the lines in the file
 for line in x:
 print(line)
	 
	












