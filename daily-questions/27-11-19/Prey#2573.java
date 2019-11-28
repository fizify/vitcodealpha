import java.io.*;
class matrix
{
    public static void main(String args[])throws IOException
    {
    int n,i,j,a=0;
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    System.out.print("Enter the matrix size:");
    n=Integer.parseInt(br.readLine());
    int mat[][]=new int[n][n];
    System.out.println("Enter the matrix values:");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            mat[i][j]=Integer.parseInt(br.readLine());
        }
    }
    int nmat[][]=new int[n][n];
    for(i=n-1;i>=0;i--)
    {
        for(j=0;j<n;j++)
        {
            nmat[j][i]=mat[a][j];
        }
        a++;
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            System.out.print(nmat[i][j]+"\t");
        }
        System.out.println("");
    }
}
}
