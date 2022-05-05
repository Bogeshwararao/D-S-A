#quick sort:
def qs(a,f,n):
    if(f<n):
        p=a[f]
        i=f+1
        j=n
        while(i<j):
            while(i<n and a[i]<p):
                i+=1
            while(j>1 and a[j]>p ):
                j-=1
            if i<j:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
        if a[j]<a[f]:
            temp=a[j]
            a[j]=a[f]
            a[f]=temp
        qs(a,f,j-1)
        qs(a,j+1,n)
    else:
        return
a=[6,30,67,44,3,45]
qs(a,0,len(a)-1)
print(a)

#print(a)
##################################################################################################################
#merge sort :
def mergeSort(arr):

    if len(arr) > 1:

        a = len(arr)//2

        l = arr[:a]
                 
        r = arr[a:]

        # Sort the two halves

        mergeSort(l)

        mergeSort(r) 

        b = c = d = 0

        while b < len(l) and c < len(r):

            if l[b] < r[c]:

                arr[d] = l[b]

                b += 1

            else:

                arr[d] = r[c]

                c += 1

            d += 1

        while b < len(l):

            arr[d] = l[b]

            b += 1

            d += 1

        while c < len(r):

            arr[d] = r[c]

            c += 1

            d += 1

arr=[4,3,7,6,5,3,1,2]
mergeSort(arr)
print(arr)


######################
#mam code
def ms(A,l,u):
    print("l=",l,"u=",u)
    if(l>=u):
        return
    else:
        m=int((l+u)/2)
        print("M=",m)
        ms(A,l,m)
        ms(A,m+1,u)
        merge(A,l,m,u)
    
def merge(A,l,m,u):
    print("L=",l,"M=",m,"U=",u)
    i=l
    j=m+1
    k=l
   
    temp=[]
    while(i<=m and j<=u):
        if(A[i]<A[j]):
            print(A[i])
            temp.insert(k,A[i])
            k+=1
            i+=1
        
        else:
            print(A[j])
            temp.insert(k,A[j])
            k+=1
            j+=1
    if(i>m):
        while(j<=u):
            temp.insert(k,A[j])
            j+=1
            k+=1
    else:
        while(i<=m):
            temp.insert(k,A[i])
            i+=1
            k+=1
    print("temp",temp)
    for i in range(l,u,1):
        A[i]=temp[i]
        

a=[10,4,50]
print("Before Sort :",a)
ms(a,0,5)
print("After Sort :",a)

            
    
