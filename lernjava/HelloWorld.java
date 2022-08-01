import java.util.Scanner;
public class HelloWorld {
    public static void main(String[] args) {
        Scanner s1=new Scanner(System.in);
        int f=s1.nextInt();
        int e=s1.nextInt();
        int $$$=0;
        int t=0;
        for (int i=f;i<=e;i++){
            if (i%2==1){
                System.out.println(i);
                $$$+=i;
                t++;
            }
        }
        System.out.println("average:"+($$$/t));
        s1.close();
    }
}
