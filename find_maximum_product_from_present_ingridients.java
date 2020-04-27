import java.util.*;

/**
 *
 * @author Akash
 */
public class find_maximum_product_from_present_ingridients {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc= new Scanner(System.in);
        int N = sc.nextInt();
        int a[]=new int[N];
        int p[]=new int[N];

        for(int i=0;i<N;i++)
            a[i]=sc.nextInt();
        for(int i=0;i<N;i++)
            p[i]=sc.nextInt();

        int flag=1,c=0,t;
    
        while (flag!=0 )
        {
            //int k=0;
            for(t=0;t<N;t++)
            {
                if (p[t]!=0)
                {
                    p[t]-=a[t];
                
                }
                else
                {
                    flag=0;
                }
            }
            if(flag!=0)
                c++;
        }
        System.out.println(c);
    }
    
}
