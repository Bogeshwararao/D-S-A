//sum of an array
#include <stdio.h>
int main()
{
int marks[10], i, n, sum = 0; 
printf("Enter n: ");
scanf("%d", &n); 
for(i=0; i<n; ++i)
{
printf("Enter number%d: ",i+1); 
scanf("%d", &marks[i]);
sum += marks[i];
}
printf("sum = %d", sum); 
return 0;
}
//average of an array
#include <stdio.h>
int main()
{
int marks[10], i, n, sum = 0,average; 
printf("Enter n: ");
scanf("%d", &n); 
for(i=0; i<n; ++i)
{
printf("Enter number%d: ",i+1); 
scanf("%d", &marks[i]);
sum += marks[i];
}
average=sum/n;
printf("average  = %d", average); 
return 0;
}
// deletion of an element from the specified location from an Array
#include <stdio.h>
int main(){
    int arr[50],i,n,loc;
    printf("Enter the size of an array: ");
    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    printf("location of array to be deleted: ");
    scanf("%d", &loc);
    while(loc<n){
        arr[loc-1]=arr[loc];
        loc++;
    }n--;
    for(i=0;i<n;i++){
        printf("%d", arr[i]);
    }
}