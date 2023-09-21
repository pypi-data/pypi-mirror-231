# Sequence Builder
# Last updated: 8/15/23
#
# This module contains DNA sequence building tools. 
#
# Classes included in this file:
#   - sequenceBuilder
#
# https://www.stephendoescomp.bio
# Stephen Cheney © 2023

import random
from structs import *
from bio_seq import *

def randDNASeq(n):
    """
    Return a random DNA sequence of given length
    \n<- n: int
    \n-> str
    """
    assert(type(n) == int)
    return ''.join([random.choice(nucleotides) 
                        for nuc in range(n)])


def randRNASeq(n):
    """
    Return a random RNA sequence of given length
    \n<- n: int
    \n-> str
    """
    assert(type(n) == int)
    return ''.join([random.choice(rnaNucleotides) 
                        for nuc in range(n)])


def randPolyPeptide(n):
    """
    Return a random polypeptide of given length
    \n<- n: int
    \n-> str
    """
    assert(type(n) == int)
    return 'M' + ''.join([random.choice(list(innerCodons.values())) 
                        for i in range(n)])


def readFile(file):
    """
    Given a file, read and return the list of lines
    \n<- file
    \n-> str[]
    """
    with open(file, 'r') as f:
            lines = f.readlines()
    return lines

# ====== Function Comment Template ======

    """
    Purpose of Function
    \nNotes: [notes]
    \n\t[more notes]    
    \n<- input: type
    \n-> type
    """