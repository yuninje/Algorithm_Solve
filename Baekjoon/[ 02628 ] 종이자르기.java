// https://www.acmicpc.net/problem/2628
import java.util.Scanner;

public class Main {
	static int[][] dir = {{2,0}, {-2,0}, {0,2}, {0,-2}};
	static int R, C; // 가로, 세로
	static int MAX_R, MAX_C;
	static int N; // 선 개수
	static int[][] line; // 선 배열
	static int[][] arr;
	static int count;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		C = sc.nextInt();
		R = sc.nextInt();
		MAX_R = 2 * R +1;
		MAX_C = 2 * C +1;
		N = sc.nextInt();
		line = new int[N][2];
		arr = new int[MAX_R][MAX_C];
		for(int n = 0; n< N; n++) {
			if(sc.nextInt() == 0) { // 가로선
				int r = sc.nextInt() * 2;
				for(int c = 0; c < MAX_C; c++) {
					arr[r][c] = 1;
				}
			}else {					// 세로선
				int c = sc.nextInt() * 2;
				for(int r = 0; r < MAX_R; r++) {
					arr[r][c] = 1;
				}
			}
		}		
		int MAX = 0;
		for(int r = 1; r<MAX_R; r += 2) {
			for(int c = 1; c <MAX_C; c += 2) {
				if(arr[r][c] == 0) {
					count = 0;
					dfs(r,c);
					MAX = MAX < count ? count : MAX;
					
				}
			}
		}
		System.out.println(MAX);
	}
	
	static void dfs(int r, int c) {
		arr[r][c] = 3;
		count += 1;
		for(int[] d : dir) {
			int rr = r+d[0];
			int rr_w = r+(d[0] / 2);
			int cc = c+d[1];
			int cc_w = c + (d[1] /2);
			if(MAX_R > rr && rr >= 0 && MAX_C > cc && cc >= 0 && arr[rr_w][cc_w] != 1 && arr[rr][cc] == 0) {
				dfs(rr, cc);
			}
		}
		
	}

}
