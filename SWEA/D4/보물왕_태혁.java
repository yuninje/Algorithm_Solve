// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWtInr3auH0DFASy
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.Arrays;
class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;	// 테스트 케이스 갯수
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int varCount = sc.nextInt();
            int [] arr = new int[varCount];
            for(int i = 0; i<varCount; i++)
                arr[i] = sc.nextInt();
            
            Arrays.sort(arr);
            
            System.out.println("#" + test_case + " " +  arr[0] * arr[arr.length -1]);
		}
	}
}