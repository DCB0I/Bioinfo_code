def hamming_dist(str1, str2):
    count = 0
    for a,b in zip(str1, str2):
        if a!=b:
            count+=1
    return count




str1 = input("Enter the sequence: ")
str2 = input("Enter the sequence: ")
print(hamming_dist(str1, str2))


