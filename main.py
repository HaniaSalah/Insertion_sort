def insertionSort(ls):
    n=len(ls)
    if n>1:
        for i in range(1,n):
            j=i-1
            k=ls[i]
            while j>=0 and k<ls[j]:
                ls[j+1]=ls[j]
                j-=1
            ls[j+1]=k
                

ls=list(input())
insertionSort(ls)
print("list",ls)