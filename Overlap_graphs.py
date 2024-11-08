def parse_fasta(fasta_strings):
    sequences = {}
    label = None
    for line in fasta_strings.strip().split("\n"):
        if line.startswith(">"):
            label = line[1:]
            sequences[label] = ""
        else:
            sequences[label] += line
    return sequences

def build_overlap_graph(sequences, k):
    adjacency_list = []
    for s1, seq1 in sequences.items():
        suffix = seq1[-k:]
        for s2, seq2 in sequences.items():
            if s1 != s2 and suffix == seq2[:k]:
                adjacency_list.append((s1, s2))
    return adjacency_list

# Example usage
fasta_strings = """
>Rosalind_4814
GTATACTACTAGGACGAGTAAGTTCGCTTCGATCTTTTGCGATGGTGGGTTGGAGTCTCG
TTCTTAGTTCTTTCCGTGATTCACA
>Rosalind_3785
CGCTAATGTGGGACGCCGATAACACACCAGTGATGTCTAACCATGCGGCAAATTTCAATA
AGAAAGCATCCTTCTCAACCTAAGCACC
>Rosalind_7468
CCCGCCAGGTAAGACAGATGGCATAATTCGCGTGGCGAGTTAACCATGTCCTATTAAGGA
GATAGGTCACCAAGTCGTTCATGGGATGCTTGG
>Rosalind_0526
CGGTCCTGAGTGCTAAGTCCAGTAGCCACTTTTTTTCGGCACACTTTGACACATACCGTG
GGGTGCGCCCAGAGAACGGCCACATCCG
>Rosalind_5267
CTTCATCGAGAGAGGATTGAACCGGATTTAGAACAGTCTCCTGGAGAATGTCCAGTCAAG
CTCGCTGTCATTCTAATCAGATCGCCGGTGTGGCG
>Rosalind_0801
CCTTTTCTGGTGGAGAGTTGAGTGCAACCTTTCATCCGTGTCAAGGACCAGGCTCACAAG
AAAGACGCAACGTTCTCACGCATATGGGAGA
>Rosalind_1671
GATGGACATAACTCGCGCTCCCCCATACGAAGGGGTCGTCTCAGGAAAAAGCATGATGTG
GCTACTTAACAGCCCATTTAATCAC
>Rosalind_8188
CCCAACGATGAATGTTGTGGCATATAATGTCTATACCGTTTATTCATGCCTTGCGTCGCC
TACAATTTTGGGTTGTAGCGATGCGGATCGG
>Rosalind_2821
CACAAATATCTGCTGGTTTACCGTAAGCTCTGCGCGACGGGTACTAAGGCAGCTGCTCTG
CGGATGTGTCAAAACGAGCAGACATTA
>Rosalind_9651
GGATGTTAGTCACGGGCTCGTTGGCCTCAGTTGTCCAAGGAGAGTTGCCAACGGATAATA
GTCAGTAGCTCCGTAAGGTACTT
>Rosalind_2301
TGAGTCCGTGCTAGTTTCTCGACCTTGTCTAACCCTAGCTCCTTGTAATATTTGGCTCAG
CGAATTTCCGGACCAATCATTGTCCCCAGGC
>Rosalind_8578
TGTTAATCCCTGCTCGACGCTATACCCGGAGAACTTCTTAAGGCAAATTCGTAGTGTATT
CCTCTTATCCAAGAGAAGTCCGCAAGTGGGCGGGACTGGA
>Rosalind_0725
TGCCCGGTACAATTGCCCAGTTGCTTCTTGCATTGACATAGCACCGTGTGCACTGCTTTA
GTAGTTTTCAACTGCGATGACT
>Rosalind_9455
GCGAGCGCTCGTTGAAAAAGCTCGCTAGATATTCTGCGCGATCCCGCACAGGCACCGGTT
GCTGAAGTAATGACCTCGTTAATAGTAAA
>Rosalind_3392
TAGGCAGTTAGTAACGACGCCAAGTCGGGACTTGTGCAGCCAAAATAAGCGCACAGTTAT
CAACTCTGCCAGGCATCAATATCTC
>Rosalind_6720
TTACATTGGGTACATAATCTCTTCAGCGGTGCAGTAGCTATATATTGCACAGCGACCTAA
CCGACCCTCTTCGCCGTATACGCTTAC
>Rosalind_1231
GTACGGCCTAAGTGACGTGGAAAGTAAGTATAGACACTCTTTAACTCAGTTACAGTGCCA
GGCGAACAGGCCATCAACTAGTGC
>Rosalind_9450
TAGTCACACACTCCAATCTTGGCATGCGATGATGGCTTAGGAGTTCTCGTGAGTCTCTAG
GACCCGCAGTCTGAGCTCAGGAAGATAG
>Rosalind_2059
CCATTCCGTATGGGTAAGAAATGACTGGGAACCAGACCACCCTGAGCCGAGCAAGGTTAC
TTGCTGTGCTGGCCACCCAGTCGGGCAACGAAAAGC
>Rosalind_7523
GCTCCGCTCCGACGGGATGTTCGCGTTGCTAGAGGAAAGGGCTTAATACCAAGGGGCTAA
GATTCTCAATTGTCTCAATTCC
>Rosalind_1826
CACGCTTAATGTTTGATAATACAAACATGTCTAGGAGGTCCGACAAGTTATAGCCTAGAT
ATACTTATCTTACCTGCAGA
>Rosalind_7114
CACTACCCCTAACAGATATGAAATATAATGGTGATAGAAACCCCCCTGACCTGCATAAAA
GCGAAAATTACATGTACCCATTACAGGCT
>Rosalind_7457
AATGCCTACAGCTGAGAAAGAGTGGTCTGAGGTCGATAGTCCATAGCACTTGACAACAGT
ATCTTCAACGATATCCCGATTCAC
>Rosalind_8688
GTGGTAACCTGCCGTTGGCCCCTCGAATTGGCCTTCAAGCTCTATTAGACGCGGCGGTAT
GCGAAACATAGGCTTTAGTAGCCGTTGGAGGGCACGTGC
>Rosalind_8860
AAGGCAGACCAACTCCTGCTCGGCATTGCGGCATGGTAGAACAGACCAGCACCTGCGTGG
CCGTGCGGAACGCGAGTGGTGACGAGATT
>Rosalind_6943
TAAGCTCTGAGGGCGACTCCCTGTGTGAGTCGGGAGACTGCTTTCCGGCGTCCCATGAGG
CTCCAATCTTGGGAATCACGGGCTC
>Rosalind_0266
ACTAACTTTTGGCTCTATGGGTAGTATGCCAGCAAGAGTCTGTCTAGTTGGTCTCGAGCC
CACTTAAAGAAATTTGTTACTCGCG
>Rosalind_3244
CTTGTCCAACTTGACCGCTACCAAATTGGTGGATGCATTAACCCTCTTGCACATTCAGAC
GTCGTGTCCTTAAACGGAAGCACAT
>Rosalind_4887
GGTGAGACGCATTCAACCCACCAAGGACTTCAACTCTGTATAGTATGGTGCTGCGCCATC
CATGCTGCTGCAGCTGGCCGCTGA
>Rosalind_0789
TTTGTCAGTCTATCTACGATTGCCCCTGGGGTTGAGTAAAATCGCTATTCACGGGTGCAC
TTCACCTGACTCCACGTGAGAATTATTAAGGG
>Rosalind_3869
TACGCCCGACAGATGCCCAAATCTTCAGGTAGTATTAACCCACTTTCACAAATGGTCCTA
CAAACTAGTTGGACTACACTTCATACCTGCGA
>Rosalind_3491
TTTCCTCTGAAATAAAAAACAGGCGCGTAAACAGGCCCTGTAGACACATGAAATAATCAT
GCAAGAACACTTACTGACGA
>Rosalind_2486
ACCCCGCCACAGGCAACGATACCGTCGCTCACTCTCGAGCATTACGGCGAGTCTTACGAA
CGGACGGTACACAAGAGGCGGCTTAGC
>Rosalind_3650
AGAAGTCAACAGTAGCCATTCTGTTGCGTACCGCTCCGCCACCCTTTACTGCAGACTATG
GCATTCCTTACTTCGGAATCGGA
>Rosalind_2858
TTCGTCTATCGGGATATACTTTAACACCGCCGATACGAAAGAGATGCGTGTGCCTCGGAA
GTAAGGTGTTCTTCATAACGA
>Rosalind_7894
AACAAGACGAATTTTTGTATGCACAGCTTTAGCATCAGGACTTACTGTAGAGCACGACAA
GGCCCCCAAGAAAGCAGTCCT
>Rosalind_5732
TGTGCGGCAAGCCAATTCAGAATTTGTACCTAAGCCAGCCTTGGAATATTCGGTCGTACG
TTTTTACGCCAGCTATGAGTAAAT
>Rosalind_3169
GCTTACCGTTCGTAAAACAGTTGAACCCCTTGGTCGGGATAAGATAGTCTCCGCATATTC
GTTGTTAGGCGGATTGACTGTATCCATGAAAGTAAAAGAA
>Rosalind_2303
GTTAACGTAGAAGAACGTGTCACCGACCAAATAATATAGCTTCTTGACGCCTACTTTTCG
CTATATAAGGAAACCGACATATTGAGGACCATCCGA
>Rosalind_6525
AGCGCCGACGATTGGATTGACGGCGCGTCAAAACGCATAAACACAGAGAACAAGCAGCTA
AAAGCCAGGTGGCTGAGTACATCTGCCACTCTGTACTCG
>Rosalind_2769
ACGTCCCATCGCGGGTGCCCCAAGCCGGTGGGAATGAACTATGGACTAGAAGATTTACCT
AGAATTGGTAACATGAAAGGCGCCTTTGATGA
>Rosalind_8883
CCTGGTGAGTATCACTGGACTCGGAATTCTCTGCAGGTCCCTGGGGACCCGACGAGGATA
AACCATTCGAGAGTGATGCTCCATCTGGAAAACGTGGA
>Rosalind_3062
GTAATCACGTGAAAGTCGCGTTATCCGAAATGTAAGGTGAGGGGTGCTACTTCCTAATTA
CGTGTTGTGCAATCAGGCATCATTAC
>Rosalind_4701
CACAGCTCCGGGTAACCTTGCACCAAGTGTCCAACGACGGTCTCGCCTGCTGTTATTTAC
GGGAGAATTGAGCTGCGGTGCGTGCG
>Rosalind_0307
ACCTCATCGTCTAAGCTGCCCGCATGGGATTTGCTATAGGATAACATAGGTTACACTTAT
CAAAGGACCCTTTAACCCGCTTCAAAAATGCTTTCGT
>Rosalind_0816
GCCACTTTGGCGGTATGTGCCCTAAGGTCGAGGATGGACGGAAGATGCCGAATATTGGTT
GCATCATCGGATCTGATACTGCTTAGCATCGGTGTA
>Rosalind_3163
ACCTAAACCAGAGGAACTCTCTTGTCGCACCATTACGTGTATGTGATTCATGTCTCTTAA
CTACGGGCTGATGCTGTATGCCACTATAAGGTGCGTCTTA
>Rosalind_7819
ATTGAAGATTGGCGCGTTATATAGCCGCTGAGGACCGGCTTCGGCTGGGGGTCTAGTTTT
CTCATGTGCACCCCGTCTAATTATGTAGTTC
>Rosalind_0362
TCGCACCAGAATTCAACCCGGACCGGACCATGTCCTGTGTAATTAGCACTAGGCCAGTGC
GGACTCGGAATTTACTAGCTCGCTCAGGGGCTT
>Rosalind_2004
TCGACAGTAATTGGCAAACCAGGTTGCTCGGACGCGTGGGAAGATCCCAAGTGGGCCACA
AGTGTCGGTCTCATTACCAGCG
>Rosalind_5002
GAGTCTCTTCTCCTGCCTCCCCGGACGCAGGTGCTGGCTACCCGACCACACTAATTACCT
CTTCCAGGGGCTGCGGCGATTAGTAGG
>Rosalind_5757
TACGCGGTAACGGTCGGTCGGGAACGCGATCTTCTGTGAAGTGCGCAGTATTGCAAGTAT
TTAGGGGATTCCCAACCCGC
>Rosalind_8438
CCGACCGTAGCGCGTAAAAAGAGGATGTTTGACATCGAACAGAGGATCCACTGAGGAATG
GCCTCAGGTCGCAGTGACGTTACCCA
>Rosalind_9997
AATCGCAACGGGATAGCGCTTCTAGGCAGTTACACGGCTATAGTAGTTGAAAATCCCATA
ACGTCGCAATTGGGCAAATCGATAACACGCTCC
>Rosalind_3490
CCACGGCCAAACCCATGACCGAGATCCGGAAATAGGAAGATTATAAAGGACCAACAGTAA
GAGGTGCGCTGCTCCCTCATTCTGCTCAGACT
>Rosalind_4603
ACCGTGTAATAACTTTACAACTTCGACGCGGTGTCCGCCAAAAGTATGTTCGTTGTAAGC
TTGCCTCTGCGGCGAAGTTTTGTCACAGG
>Rosalind_7777
TTGTAAATGATACCAGGTATTCTGCATGACTATGTGTTTAGATATGTACACCTCGAATGA
TGGCCAGCACTGCGTGAACCCG
>Rosalind_2439
AGGTGTGGGGCTAGAGATTCCCGTGACGAAGGCATATTTCTCTCATCCCATCGCTGCGAG
CATAGGGCTGCGTGGGGCAGTAACAT
>Rosalind_8209
GTTGCCCTAAAATGTGACTTGACGTATCGCCACATGATTCTTTGTCGGGTGCCACGCGCG
TAACCAGGGATGCATGTCACACGTATCCATCGT
>Rosalind_9404
TTTGGTCAGCGTTACCAGAATGCCGGAGTCCCGCCTGGAAATAGTTATGAAATCCCGGTG
ACTTTCAACGCTGGCAATAGGATTCAATCACTCGGGACAT
>Rosalind_1533
ATGCCATAGTATTAAAGGCAATATTAATACGACACCATACCTATTTAATCTCGTTTTCCT
GGAATTTCAGCAGGCTAAACAAGGGTTCTGAGCTGT
>Rosalind_1135
ATAGAGATATTGGGCAGGACGTAACGCTCGTAACACACTTCAAAAGTACCGCCAGTACTC
TCGATTCGCCTTTCTGTCTCGTCG
>Rosalind_8238
AGGAAGAACCTAGCGAAAACCTTAGAGATTTCGAATGGATACGTTCTGGCTGAGCGACTA
CCGGAGAGCGGTAGTGTAACC
>Rosalind_8414
CCTACTCGTGCGAACGTAGGATTCAATAGCAAAATTTCTTATTAAGACCAACGCCAACCT
GACGTAACAAAGATTCTTCTGGCAGCAC
>Rosalind_7930
CAAGCACCATCCTGGCGATGAGCTTTGCCGATACGGGAGTCTGGGTAAGCCCAGGTACGT
TTGTATGATCACTATTGTGCTGCGGGCTGTAGGACCTT
>Rosalind_1030
CACCTAGTTTACAATTTACTTGCGGCTAGGATCAGCCCCCCCTTTCCGCCCCGTGAAATC
CTGCTCGTGTCATGGCCTCAGTTACCCCTGCAGAG
>Rosalind_9912
CAAAACGGGTTTATCACGCACGTGGTCGGTGGCACAGATCGGTTGAACTTTCCGTGGCGA
GCACTTCAAAGCTTGCAGTACCCCACGTC
>Rosalind_7191
TAAGTCGCCCTTCACAGAAACGCCCATCACGGGTAGAGGCGTGGGACTCAGGTTTCCAGA
CTGCAAATAGCTCACAGACAATC
>Rosalind_2810
TGAGGGGTCTGCACTAAAGGCATCTTTCACTATCTTTGAGGTTCCCGATGGTATAGTAGG
GGAGGTGAGTCGGGATCGGGTGT
>Rosalind_4464
GACAAAGCGAGGAAGTGGATAGTGACAGTGTCGCAGATGTACGCGATAGCACATCTCCAG
CAATGCACAATATCCAGAGCACTGGTCGGCCCTAACTTA
>Rosalind_9524
TTTGCCCGGCGAATCTACTGGTTTCATGGGCTCGGACGGAGCTTTCCAATACTTACAACG
ACGGCATATACTGGGAACTTACCCT
>Rosalind_1765
CTGAAGTTGACATTAGGAATGCGTGAGGCTAAATGTCTAAATTTAGTAATAACGACGTCC
ATAAAATCATTCTTCATCGGGGAGGAGTCAACAATTTC
>Rosalind_0822
GGTGCCATGGACTACCAGGTTGCATTTGCCGCGTCAGCCTGCGATTTTCAGCTGTCGGAC
GGGGAACGGTGTATACGCTATGTCCGGTGGC
>Rosalind_7428
GCGAATCTTGGACCGGAGAAAATGTCGGCTACATTTGTCCATGGTCAGACCATTAGGTCC
TGAGGCCATATCAATTCGTCACCGAGCACGTT
>Rosalind_5311
CAGTTCGCTTCCGTGTCGACGTGCTCAAGCGAACTTGGCACCGAATGTCTAGAGGATCCA
TTGTATTAAAGTCTGAGTTACGGGCC
>Rosalind_6909
TTGATATTCACTTGAGTTACATAGTCTGAGCCTCGGATATCCCTCCCGCCATCTGTTTTC
GAATAGGTAGTTCCAGCTTTGCCATTCCGCGGA
>Rosalind_6849
GTGCTCTTTTACGACAAGTACTCGATTGAAGCGCCTAAGAATGTGTGGCTCTTATCTAGT
GCCAACGATACGTAAATAGAACAGAACCGACGGGATGG
>Rosalind_6003
GTCTAACACCTACGAAGCCCCCTGTCATGCCTTATTCCCCAATCTTTATCCACCAGTGAG
CAATGGGTCCAGAGACTGTGTAAGCTCACT
>Rosalind_6789
CATAGAAGGAACGTGCGAAAGCCGTACTCCTAGGATACGATCCTCCCTGGACGTACGTTA
CAGTGCGCTGATTGTCGCGTGCAT
>Rosalind_3606
GGCTTTACATGACTAGGCCGTCTATACAACACAGCGCGAGGACTTTTTGCTCTCGGTTTC
GTAGTCTAGTCTGCCTGTGATGTTGCTTGAGGGGAGAGG
>Rosalind_8354
CGAGTGCTCCTCAAACACCTATAGCTATTTGCGCACGTCGGTTCTTCAAAAAGTGACGCT
CAGACAGCCACCTCTAGGTCACTAGAGGTTTT
>Rosalind_8300
TCAATGAAGTTTCTTGTCAGAAGGGGGAGCGTAACGTCGTGATTGGCAGCGCCTCAGGAT
TATACGTTTTGAACTTGTAGGAAGAA
>Rosalind_0061
AGACAAACGTTAGAGCGCCGGCATTGTATATGGTGGGCTGTATACTTCCGTTTTACTTCT
AAACCTCTGGGTACGCTGCGTTTACATACGACCTAT
>Rosalind_0776
TTATCGCGCGCCACAGGACCTGCTCATGGCGTACGTAACGATGGAGCACTGGCTTATCGA
GATGAGGCTACACGGAACTATTGATTGGCCATGAG
>Rosalind_1669
TCTCGATCTATAGTGTATGCGAAGAGATAAGAGCTCCGCATAGCACCTAAGCTTCTGCAC
GTTTGTGTTATTTTAGAAGGCGAAC
>Rosalind_6996
GGCTACCTCATCGTGATTAGACATGATACTGTCCGCGTGCGTCTGACGACCACCGTAACA
CGCCTTGGGTAGGTAAGTCATAGTCG
>Rosalind_3380
CGTCAAGACAGCCCATCCCACATATATAGCTAGCACTCTTCCTAATATGCGCGGAGGTAC
GCGGATAGGTGCCACTTTCGATCGACGGTCAA
>Rosalind_5800
GGACGTTGCGAGGTGCTCTGTTGTGGCTTGATGCAGGAAACTGACACCGGAACGCGTGTT
TCCAACTAATAAGGCTAAGATCGTT
>Rosalind_1947
TATCTAAGCAAATACGCACCTACACACGCCCGAGACGCTGTTTGGCAGACGGTTCGGGCC
ACCGCCCATTTAAGATGCATCCTAAA
>Rosalind_9300
AAATCTATCTACTTACCAGTCGAACGGCCACAGACGTACCCTGAGACGTAGCTCGCGGTT
GGTGTCGACCTGTTGGCAAATCCCCGGCAAGC
>Rosalind_4355
CTTGCTAGCAGCCGGGCACTACGAACCCGCTATGGCTGTCCCTTACCACGAAAAGAACAA
TCCGCCCAGATCACTAGCGGGCTTA
>Rosalind_9777
CGAGCAATGGGGGTAACGTGGATGCCTTTGAACTGGTTTGCTAGTTGCTGCGACTGGATT
TGCAAGAGGTAGGATCATCAA
>Rosalind_4219
TGAGATCTGAAAAGCAGAATCGAAGTTGAATCGATTAACAGACTCCAACAGTGCGACGAA
AGATCTCCTTCACAGAAGCCAGCTCAGGCCCCCATAATC
>Rosalind_7828
ACCGCCATCCTATTTGAACGGTAGCCCGGTCTCGCGGCCCCTTTTAATTTACGGAGACAC
ACACCCGGACTTGTCGAACAGGCGGTAGCCCTGCGATGT
>Rosalind_6369
AATGCGGCTTGCGAGGAGCCGAACAATAACTTATCGAGAACCGCTGTAGGTTGCCTGGTA
GATACCCCTGCCTGCGTGCGCTTTTCA
>Rosalind_9178
GCGGTGAGGCATCTTTCCGACAACCGAAACGACGAGTAACATACACTACCACACGACATC
AGTACAGTTCGGGCTAGCACCAGTTGCGC
>Rosalind_8402
GTAATTGCAAACATCCTACTGAGAGTTTTACTGCTAGCCCCGGGCGGATGGGACAAAGCC
TGCAATACCGAAGGACTAGCAAGCACCACCCTGAGGCTAG
>Rosalind_4197
CTTATACCGGTCGCTCCCCAGAGCCATATTGCTGGGTTGTATGTTTCGACCCAATAAGCT
TCCTGTGAAGAGGAGACGATGATCAACTTTCCC
>Rosalind_4759
TCACTGGTTACTGCAATCCGCTGCACAATTCTCACCCCCAAAATACTTTAAGAAAGGGTA
CGTGATACTTTACAGACACGAAAAGAAA
>Rosalind_6317
ACGTTGCGCTCACGCGGCACCCTTTAGAGTTGATTGTTAGTCCGCACTAGAAACTTCTTG
TTAGCAATTTAATGTAAGTGCAGCACGGGGGT"""

sequences = parse_fasta(fasta_strings)
overlap_graph = build_overlap_graph(sequences, 3)

for edge in overlap_graph:
    print(edge[0], edge[1])
