// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWslJ57qFS0DFASy
import java.util.Scanner;
import java.io.FileInputStream;
class Solution
{
	public static void main(String args[]) throws Exception
	{
		//System.setIn(new FileInputStream("res/input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
        int[] answer = new int[T+1];
		for(int test_case = 1; test_case <= T; test_case++){
			int N = sc.nextInt();	// 배열 길이
            int M = sc.nextInt();	// 총 금액
            int[] arr = new int[N];
            int index = 0;   
            for(int i = 0; i<N; i++)
                arr[i] = sc.nextInt();
                         
           	while(index != N){
                int total = 0;
             	for(int i = index; i<N; i++){
               		total += arr[i];
                    if(total == M)
                        answer[test_case]++;
                    else if(total > M)
                        break;
                }
                index++;
            }
        }
        for(int test_case = 1; test_case <= T; test_case++){
        	System.out.println("#"+test_case + " " + answer[test_case]);
        }
	}
}