import java.util.Arrays;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args){
     	Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        for(int test = 1; test<T+1; test++){
         	int total = sc.nextInt();
            int good = sc.nextInt();
            
            int[] goodArr = new int[good+1];
			int goodIdx = 0;
            for(int i = 0; i<good; i++){
                goodArr[i] = sc.nextInt();
            }
            goodArr[good] = total+1;
            Arrays.sort(goodArr);
            int[] badArr = new int[total-good];
            
            for(int i = 0; i<total; i++){
            	if(i+1 == goodArr[goodIdx])
                    goodIdx++;
                else{
                    badArr[i-goodIdx] = i+1;
                }
            }
            
            System.out.print("#" + test+ " ");
            for(int i = 0; i<total - good; i++)
            	System.out.print(badArr[i] + " ");
           	System.out.println();
        }
            
    }

}
