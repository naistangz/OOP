"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21

"""
sample_dna = "AGCGTGTGGATTAATTACGGGTTCATTCTGACTAGCACAATATGTCTCTAATGATAGCAGCGTGT"

class Nucleod:

    def count_dna():
        n = input("Please enter your DNA data:\n")
        print("Adenine (A): " + str(n.count("A")),"Cystosine (C): "+ str(n.count("C")), "Guanine (G): " + str(n.count("G")), "Thymine (T): " + str(n.count("T")))



Nucleod.count_dna()
# Result Adenine (A): 17 Cystosine (C): 11 Guanine (G): 16 Thymine (T): 21
