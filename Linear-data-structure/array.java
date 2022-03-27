import java.util.Scanner;

//proggram to print the hello world in java

public class  array{
    public static void main(String []args) {
       System.out.println("Hello World"); // prints Hello World
    }
 }

// //proggram to print the looping 

public class array{
   public static void main(String [] args){
           for(int i=0; i<=9 ; i++){
            System.out.println(i);
           }
   }
}

//comming to array we have the 5 operation:
// 1)insertion 
// 2)deletion
// 3)sortting
// 4)searching
// 5)Traverse

//insertion an element in an array :
public class array{
   public static void main(String [] args) {
         int size,in_element;
         Scanner sc= new Scanner(System.in);
         System.out.println("Enter the size of an array");
         size = sc.nextInt();
         int arr[]= new int[size+1];
         for(int i=0;i<size;i++)
         {
            arr[i]=sc.nextInt();
         }
         System.out.print("Enter the element which you want to insert:");
         in_element=sc.nextInt();
         arr[size] = in_element;
        System.out.print("After inserting : ");
        for(int i = 0; i <size; i++)
        {
            System.out.print(arr[i]+",");
        }   
   }
}

//deletion of an element in an array:
public class array{
   public static void main(String[] args)
   {
      int i, j, size=10, element;
      int[] arr = new int[size];
      Scanner scan = new Scanner(System.in);
      
      System.out.print("Enter 10 Elements: ");
      for(i=0; i<size; i++)
         arr[i] = scan.nextInt();
      
      System.out.print("Enter the Element to Remove: ");
      element = scan.nextInt();
      
      for(i=0; i<size; i++)
      {
         if(element==arr[i])
         {
            for(j=i; j<(size-1); j++)
               arr[j] = arr[j+1];
            System.out.println("\nRemoved the element successfully!");
            break;
         }
      }
      
      System.out.println("\nThe new array is: ");
      for(i=0; i<(size-1); i++)
         System.out.print(arr[i]+ " ");
   }
}
