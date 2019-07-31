// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD
import java.util.Scanner;
import java.util.Arrays;
class Solution{
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        for(int test =1; test<=10; test++){
            int N = sc.nextInt();
            sc.nextLine();
            String str = sc.nextLine();
            int[] counts = new int[8];
            for(int i = 0 ; i<N; i++){
                switch(str.charAt(i)){
                    case 40:
                        counts[0] ++;
                    break;
                    case 41:
                        counts[1] ++;
                    break;
                    case 60:
                        counts[2] ++;
                    break;
                    case 62:
                        counts[3] ++;
                    break;
                    case 91:
                        counts[4] ++;
                    break;
                    case 93:
                        counts[5] ++;
                    break;
                    case 123:
                        counts[6] ++;
                    break;
                    case 125:
                        counts[7] ++;
                    break;
                }
            }
            if(counts[0] == counts[1] 
            && counts[2] == counts[3]
            && counts[4] == counts[5]
            && counts[6] == counts[7])
                System.out.println("#" + test + " 1");
            else
                System.out.println("#" + test + " 0");
        }
    }
     
}