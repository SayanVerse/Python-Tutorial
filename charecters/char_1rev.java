import java.util.*;
public class char_1rev{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the value:");
        int a= sc.nextInt();
    for(int i=a; i>0; i--){
            char s='A';
            for(int j=1; j<=i; j++){
                System.out.printf("%c ", s);
                s++;
            }
            System.out.println();
        }
        sc.close();
    }
}