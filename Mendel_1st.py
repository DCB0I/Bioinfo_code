def Get_Probability(k,m,n):
    Tot_Pol = k+m+n
    Branch_1 = k/Tot_Pol * (((k-1)/(Tot_Pol-1)) + (m/(Tot_Pol-1)) + (n/(Tot_Pol-1)))
    Branch_2 = m/Tot_Pol * ((k/(Tot_Pol-1)) + (3/4) * ((m-1)/(Tot_Pol-1)) + (1/2) * (n/(Tot_Pol-1)))
    Branch_3 = n/Tot_Pol * ((k/(Tot_Pol-1)) + (1/2) * (m/(Tot_Pol-1)))
    return ((Branch_1+Branch_2+Branch_3))

print(Get_Probability(16,16,30))