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
        temp=a[j]
        a[j]=a[f]
        a[f]=temp
        qs(a,f,j-1)
        qs(a,j+1,n)
    else:
        return
a=[3,6,11,12,13]
qs(a,0,len(a)-1)
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