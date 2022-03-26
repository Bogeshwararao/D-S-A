import java.util.Scanner;

//proggram to print the hello world in java

// public class  array{
//     public static void main(String []args) {
//        System.out.println("Hello World"); // prints Hello World
//     }
//  }

//proggram to print the looping 
// public class array{
//    public static void main(String [] args){
//            for(int i=0; i<=9 ; i++){
//             System.out.println(i);
//            }
//    }
// }

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
         



      
   }
}
