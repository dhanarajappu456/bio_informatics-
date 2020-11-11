#set approach

dna1,dna2=input("enter the genomic sequence with space seperated:\n").split(' ')
def hamming_calc(dna1,dna2):
    a=set(enumerate(dna1))
    b=set(enumerate(dna2))
    return(a.difference(b))



#naive approach

def naive_approach():
    count=0
    for i in range(len(dna1)):
        if(dna1[i]!=dna2[i]):
            count+=1
    return(count)        
print('hamming distance by set method is:',len(hamming_calc(dna1,dna2)))
print('hamming distance by naive approach is:',len(hamming_calc(dna1,dna2)))