"""Module to convert dna into rna
"""
def to_rna(dna_strand):
    """Function to convert dna into rna

    Args:
        dna_strand (str): given dna

    Returns:
        str: converted rna
    """


    rna = ""

    for dna in dna_strand:
        if dna == "A":
            rna = rna + "U" 
        if dna == "C":
            rna = rna + "G"
        if dna == "T":
            rna = rna + "A"
        if dna == "G":
            rna = rna + "C"

    return rna
