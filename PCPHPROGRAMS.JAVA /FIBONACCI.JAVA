package PCPH;
import java.util.Scanner;
public class FIBONACCI
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(Syatem.in);
        System.out.print("Enter the number=");
        int N = sc.nextInt();
        int N1 = 0;
        int N2 = 1;
        for(int i = 0 ; i<N ; i++)
        {
            System.out.println(N1 + " ");
            int N3 = N2 + N1;
            N1 = N2;
            N2 = N3;
        }
    }
}