def dna_to_protein(dna_sequence):
    mrna_sequence = dna_sequence.replace("T","U")
    
    codon_table = {
        "AUG": "M", "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "AUU": "I",
        "AUC": "I", "AUA": "I", "GUU": "V", "GUC": "V", "GUA": "V",
        "GUG": "V", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACU": "T",
        "ACC": "T", "ACA": "T", "ACG": "T", "GCU": "A", "GCC": "A",
        "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y", "UAA": "STOP",
        "UAG": "STOP", "UGA": "STOP", "CAU": "H", "CAC": "H", "CAA": "Q",
        "CAG": "Q", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "UGU": "C",
        "UGC": "C", "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R",
        "CGG": "R", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    protein = []
    for item in range(0, len(mrna_sequence),3):
        codon = mrna_sequence[item:item+3]
        if codon_table.get(codon)=="STOP":
         break
        protein.append(codon_table.get(codon,""))
    return protein
dna_sequence = "ATCGCCTTCCTCTGTAGTCCGCTGGGGGTGCTCGCAGAAATCGCGTTATCGAGGGCTCGC"
protein = dna_to_protein(dna_sequence)

print(dna_sequence)
print(protein)
