def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)
#######################################
Splitting  [2, 8, 3, 4, 6, 1, 5, 7]
Splitting  [2, 8, 3, 4]
Splitting  [2, 8]
Splitting  [2]
Merging  [2]
Splitting  [8]
Merging  [8]
Merging  [2, 8]
Splitting  [3, 4]
Splitting  [3]
Merging  [3]
Splitting  [4]
Merging  [4]
Merging  [3, 4]
Merging  [2, 3, 4, 8]
Splitting  [6, 1, 5, 7]
Splitting  [6, 1]
Splitting  [6]
Merging  [6]
Splitting  [1]
Merging  [1]
Merging  [1, 6]
Splitting  [5, 7]
Splitting  [5]
Merging  [5]
Splitting  [7]
Merging  [7]
Merging  [5, 7]
Merging  [1, 5, 6, 7]
Merging  [1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
#################################
