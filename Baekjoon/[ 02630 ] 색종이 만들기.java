import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    // https://www.acmicpc.net/problem/2630
	static int N;
	static int[][] map;
	static int idx = 2;
	static int count0 = 0;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for(int i=0;i<N;i++){
            String[] line = br.readLine().split(" ");
            for(int j=0;j<N;j++){
            	map[i][j] = Integer.parseInt(line[j]);
            }
        }
		
		dfs(0,N-1,0,N-1, N);
		
		System.out.println(count0);
		System.out.println(idx-2);
		
		
	}
	
	static void dfs(int sr,int er,int sc,int ec, int length) {
		int mr = (sr + er) /2;
		int mc = (sc + ec) /2;
		
		boolean flag0 = false;
		boolean flag1 = false;
		for(int r = sr; r <= er; r++) {
			for(int c =sc; c <= ec; c++) {
				if(map[r][c] == 0) {
					flag0 = true;
				}else {
					flag1 = true;
				}
			}
		}
		
		if(flag0 && flag1) {
			dfs(sr,mr, sc, mc, length/2);
			dfs(sr,mr,mc+1,ec, length/2);
			dfs(mr+1,er,sc, mc, length/2);
			dfs(mr+1,er,mc+1,ec, length/2);
		}else if(flag0) {
			count0++;
		}else if(flag1) {
			for(int r = sr; r <= er; r++) {
				for(int c =sc; c <= ec; c++) {
					map[r][c] = idx;
				}
			}
			idx ++;
		}
	}

}
