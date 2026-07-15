"""Module to find the proteins in a RNA string
until it meets the stop signs
"""
def proteins(strand):
    """Given the RNA string, returns the proteins
    in the RNA until it gets to the stop signs

    Args:
        strand (str): the RNA string

    Returns:
        list: the list of proteins
    """

    stop_signs = ["UAA", "UAG", "UGA"]
    splitted_strand = [(strand[index:index+3]) for index in range(0, len(strand), 3)]
    codons = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan"
    }


    result = []
    for rna in splitted_strand:
        if rna in stop_signs:
            break

        if rna in dict(codons):
            result.append(dict(codons)[rna])

    return result
