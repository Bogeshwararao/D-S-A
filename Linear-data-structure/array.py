#proggram for insertion sort
# list= [1,2,3,4,9,5]
# for i in range(1,len(list)):
#     j=i-1
#     while j>=0 and list[j]>list[j+1]:
#         t=list[j]
#         list[j]=list[j+1]
#         list[j+1]=t
#         j=j-1
# print(list)


#proggram to insert an elemnet
list=[1,2,3,4,5]
print(list)
x=int(input("Enter the value to be inserted"))
p=int(input("Enter the position to be insereted"))
list.append(0)
for i in range(len(list)-1,p-1,-1):
    list[i]=list[i-1]
list[p-1]=x

print(list)