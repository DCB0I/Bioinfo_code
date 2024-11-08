def find_substring_locations(s, t):
    locations = []
    len_s = len(s)
    len_t = len(t)

    for i in range(len_s - len_t + 1):
        if s[i:i + len_t] == t:
            locations.append(i + 1)  # Adjusting position to be 1-based

    return locations

# Example usage:
s = "CAAGCTTAAAATCCAAGCTTGCGCAAGCTTTGCAAGCTTACAAGCTTAATCGCAAGCTTTCACAAGCTTGCAAGCTTCAAGCTTGCAAGCTTTTGTCAAGCTTCAAATCAAGCTTATCAAGCTTCAAGCTTTTTTATTCAAGCTTGATCAAGCTTGGCAAGCTTTTCAAGCTTTACAAGCTTGCAAGCTTCAAGCTTTTGGCCAAGCTTTTCAAGCTTCAAGCTTCTGCCAAGCTTCAAGCTTCCCAAGCTTCAAGCTTCCAAGCTTCCAAGCTTGTCTCTCAAGCTTCAAGCTTAGGGACAAGCTTATTCAGAAAGCCAAACAGACAAGCTTTCAAGCTTCAAGCTTCAAGCTTGTACAAGCTTCAAGCTTAGTCAAGCTTGCAAGCTTCATCCAAGCTTCCAAGCTTCAAGCTTCCAAGCTTCAAGCTTCGATGTCCAAGCTTACAAGCTTCTCATCAAGCTTTACCTCAAGCTTGCAAGCTTATCAAGCTTTCTGCAAGCTTCAAGCTTTCGTAAAAGACAAGCTTAACAAGCTTCAAGCTTTCAAGCTTGGCCAAGCTTCGATTTTGGGCAAGCTTCGTCTTCCCTGACCAAGCTTCGCAAGCTTATATGCCCACCGACCAAGCTTAGGCGCTCAAGCTTGAACGTCAAGCTTCGACAAGCTTGTACAAGCTTATACAAGCTTACAAGCTTTTAACAAGCTTGTCAAGCTTGGCCCAAGCTTGGCAAGCTTTCCCAAGCTTAAACAAGCTTCGAGTCAAGCTTCAAGCTTGCAAGCTTCAAGCTTAGGAGCAAGCTTACAAGCTTAT"
t = "CAAGCTTCA"
result = find_substring_locations(s, t)
print(result)

# s1,s2 = open('rosalind_subs.txt').read().split('\r\n')
#
# for i in range(len(s1)):
#     if s1[i:].startswith(s2):
#         print i+1