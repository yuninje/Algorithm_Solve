import java.util.Scanner;
import java.io.FileInputStream;
class Solution{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = sc.nextInt();
            int M = sc.nextInt();
            int MAX =  N > M ? (M-1)/2 + 1 : (N-1)/2 +1;
            int result = 0;
            
            boolean[][] arr = new boolean[N][M];
            for(int i = 0; i<N; i++){
                String str = sc.next();
                for(int j = 0; j<M; j++){
                 	if(str.charAt(j) == '1')
                        arr[i][j] = true;
                }
            }
            
            while(true){
                boolean breakFlag = false;
                for(int i = 0; i <= N - ( MAX * 2 - 1) ; i++){
                    for(int j = MAX-1 ; j <= M-MAX ; j++){
                    	if(arr[i][j]){
                         	   // check
                            breakFlag = checkMax(arr,i,j,MAX);
                        }
                        if(breakFlag)
                            break;
                    }
                    if(breakFlag)
                            break;
                }
                
                if(breakFlag){
                    System.out.println("#" + test_case + " " + MAX);
                 	break;   
                }
          		MAX --;
                if(MAX == 0){
                    System.out.println("#" + test_case + " " + MAX);
                 	break;   
                }
            }
		}
	}
    static boolean checkMax(boolean[][] arr, int x, int y, int MAX){
        for(int i = x, stack = 0; i <= x + MAX-1; i++){
            if( arr[i][y-stack] && arr[i][y+stack])
                stack++;
            else
                return false;
        }
        
        for(int i = x+MAX, stack = MAX - 2; i<x + 2*MAX-1; i++){
             if( arr[i][y-stack] && arr[i][y+stack])
                stack--;
            else
                return false;
        }
        return  true;
    }
}