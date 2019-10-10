package SWEA_º¸±Þ·Î;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution {
	
	static class Pos{
		int r;
		int c;
		public Pos(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}
	
	static int N;
	static int[][]Map;
	static int[][] dp;
	static final int INF = Integer.MAX_VALUE;
	static int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = Integer.parseInt(sc.nextLine());
		for(int test = 1; test<T+1; test++) {
			N = Integer.parseInt(sc.nextLine());
			Map = new int[N][N];
			for(int r = 0; r<N; r++) {
				String line = sc.nextLine();
				for(int c = 0; c<N; c++) {
					Map[r][c] = line.charAt(c)-'0'; 
				}
			}
			dp = new int[N][N];
			for(int r = 0; r<N; r++) {
				for(int c = 0; c < N; c++) {
					dp[r][c] = INF;
				}
			}
			dp[0][0] = 0;
			// bfs
			Queue<Pos> que = new LinkedList<>();
			Queue<Pos> que_;
			que.add(new Pos(0,0));
			while(!que.isEmpty()){
				que_ = new LinkedList<>();
				for(Pos p : que) {
					int r = p.r;
					int c = p.c;
					for(int[] d : dir) {
						int rr = p.r + d[0];
						int cc = p.c + d[1];
						if(0 <= rr && rr < N && 0 <= cc && cc < N && dp[rr][cc] > dp[r][c]+Map[rr][cc]) {
							dp[rr][cc] = dp[r][c]+ Map[rr][cc]; 
							que_.add(new Pos(rr,cc));
						}
					}
				}
				que = que_;
			}
			
			System.out.println("#" + test + " " + dp[N-1][N-1]);
			
		}
		
		
	}

}
