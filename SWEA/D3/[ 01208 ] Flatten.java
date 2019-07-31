// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh
import java.util.Scanner;
import java.util.Arrays;
class Solution{
 	public static void main(String[] args){
     	Scanner sc = new Scanner(System.in);
        for(int test = 1; test<11; test++){
         	int dump = sc.nextInt();
            int[] arr = new int[100];
            for (int i = 0; i<100; i++)
             	   arr[i] = sc.nextInt();
            for(int d = 0; d<dump; d++){
            	Arrays.sort(arr);
                arr[0] ++;
                arr[99]--;
            }
            Arrays.sort(arr);
            System.out.println("#" + test + " " + (arr[99]-arr[0]));
        }
    }
}