import java.io.*;
class fibb
{
    public static void main(String args[])throws IOException
    {
        int a=0,b=0,c=1,fib=0;
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the length of the series:");
        int n=Integer.parseInt(br.readLine());
        System.out.print(b+" "+c+" ");
        for(int i=0;i<(n-2);i++)
        {
            int temp1,temp2;
            fib=a+b+c;
            System.out.print(fib+" ");
            temp1=c;
            c=fib;
            temp2=b;
            b=temp1;
            a=temp2;
        }
    }
}
