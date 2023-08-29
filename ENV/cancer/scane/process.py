from __future__ import division
import numpy as np
import re as re
import matplotlib.pyplot as plt
from dna_features_viewer import BiopythonTranslator
from Bio import SeqIO
import numpy as np
from .codonTable import codonTable


# translate() function translates a DNA or RNA coding sequence and returns the peptide sequence

def translate(seq):

	# Handle both DNA and RNA
	sequence = seq.replace('U', 'T').upper()

	# use regular expressions to parse codons from sequence
	codons = re.findall('...', sequence)		
	res = []

	# Iterate through the codons
	for codon in codons:
		res.append(codonTable[codon])
	result = ''.join(res)

	return result
	
def transcribe(seq):

    result = seq.replace('T', 'U')

    return result

# computeGC() function returns GC base pair proportion as a decimal

def computeGC(seq):

	# Initialize count to 0
	n = 0

	# Iterate throug the sequence
	for char in seq:
		if char == 'G':
			n += 1
		elif char == 'C':
			n += 1
		else:
			pass
	test=float(n) / float(len(seq))
	

	# Convert numbers to floats, carry out division, and return result
	return str(float(n) / float(len(seq)))






def parseMotif(motif, seq):

	# Stringify inputs from DOM HTML input
	motif, seq = str(motif), str(seq)

	# Initialize result to an empty list
	result = []

	# Iterate through each frame among those where motif occurss
	for frame in re.finditer(motif, seq):
		# Append the indices of occurrence to result
		result.append([frame.start(), frame.end()])

	return result

def baseDistribution(seq):

    # Measure sequence length and initialize result variables to 0
    length = len(seq)
    a, t, c, g = 0, 0, 0, 0         # result variables

    # Iterate through the sequence, counting each result variable
    for i in range(0, length):
        if seq[i] == 'A':
            a += 1
        elif seq[i] == 'T' or seq[i] == 'U':
            t += 1
        elif seq[i] == 'C':
            c += 1
        elif seq[i] =='G':
            g += 1
        else:
            pass

    # Compile results into a list
    result = [a, t, c, g]

    # Return the results
    return result
