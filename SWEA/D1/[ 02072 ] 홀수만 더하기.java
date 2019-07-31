// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq
import java.util.Scanner;
class Solution{
 	public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
     	int T =  sc.nextInt();
        for(int t = 1; t<=T ; t++){
            int sum = 0;
            for(int j = 0; j<10; j++){
                int a = sc.nextInt();
            	sum += ( a%2==1 ? a : 0 );
            }
            System.out.println("#" + t + " " + sum );
        }
    }
}