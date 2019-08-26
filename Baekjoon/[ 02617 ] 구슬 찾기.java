// https://www.acmicpc.net/problem/2617
import java.util.Scanner;

public class Main {
	static int N; // 홀수, N개의 동전   1<= N <= 99
	static int M; // 비교하는 쌍의 개수
	static int count;
	static int[][] inner;
	static boolean[] visit;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		inner = new int[N+1][N+1];
		visit = new boolean[N+1];
		for(int m = 0; m<M; m++) {
			int b = sc.nextInt();
			int s = sc.nextInt();
			inner[b][s] = 1; // 크다
			inner[s][b] = 2; // 작다.
		}
		
		int result = 0; 
		for(int n = 1; n <= N; n++) {
			reset();
			dfs(n, 1);
			if(count > N/2) {
				result++;
				continue;
			}
			reset();
			dfs(n,2);			
			if(count > N/2) {
				result++;
			}
		}
		
		System.out.println(result);
		
	}
	
	static void dfs(int now, int size) {
		visit[now] = true;
		for(int n = 1; n<= N; n++) {
			if(inner[now][n] == size && !visit[n]) {
				count += 1;
				dfs(n,size);
			}
			if(count > N/2) {
				return;
			}
		}
	}
	
	static void reset() {
		for(int n = 1; n<=N; n++)
			visit[n] = false;
		count = 0;
	}
}
