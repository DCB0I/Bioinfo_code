def consensus_sequence(sequences):
    consensus = ""
    sequence_length = len(sequences[0])  # Assuming all sequences have the same length

    for i in range(sequence_length):
        counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

        # Count occurrences of each nucleotide at position i
        for sequence in sequences:
            nucleotide = sequence[i]
            counts[nucleotide] += 1

        # Choose the nucleotide with the highest count as the consensus
        consensus_nucleotide = max(counts, key=counts.get)
        consensus += consensus_nucleotide

    return consensus


def read_sequences_from_file(filename):
    sequences = []
    with open(filename, 'r') as file:
        sequence = ""
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences


# Example usage
filename = 'C:/Users/DC/Desktop/MisX/rosalind_cons.txt'  # Change this to the path of your file
sequences = read_sequences_from_file(filename)
consensus = consensus_sequence(sequences)
print("Consensus sequence:", consensus)
