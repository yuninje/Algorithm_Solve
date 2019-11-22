// R : Map 세로 크기         5 <= R <= 50
// C : Map 가로 크기         5 <= C <= 50
// HOLE_R : HOLE 의 세로     
// HOLE_C : HOLE 의 가로
// L : 탈출 후 소요된 시간   1 <= L <= 20
 
 
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;
  
public class Solution {
    static int R;
    static int RR;
    static int C;
    static int CC;
    static int OHOLE_R;
    static int OHOLE_C;
    static int L;
    static int OMap[][];
    static int Map[][];
    static boolean visit[][];
    static int[][] dir = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
     
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(bf.readLine());
        for(int test = 1 ; test <= T; test++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
              
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            OHOLE_R = Integer.parseInt(st.nextToken());
            OHOLE_C = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());
            RR = R * 2 + 1;
            CC = C * 2 + 1;
            OMap = new int[R][C];
            for(int r = 0 ; r < R ; r++) {
                st = new StringTokenizer(bf.readLine());
                for(int c = 0 ; c <C ; c++) {
                    OMap[r][c] = Integer.parseInt(st.nextToken());
                }
            }
            Map = new int[ RR ][ CC ];
            visit = new boolean[ RR ][ CC ];
 
            for(int r = 0; r<R; r++){
                int rr = r * 2 + 1;
                for(int c = 0; c < C; c++){
                    int cc = c * 2 + 1;
                    Map[ rr ][ cc ] = OMap[r][c];
                    if(OMap[r][c] == 1){
                        Map[ rr -1 ][ cc ] ++; // UP
                        Map[ rr + 1 ][ cc ] ++; // DOWN
                        Map[ rr ][ cc - 1 ] ++; // LEFT
                        Map[ rr ][ cc + 1 ] ++; // RIGHT
                    }else if(OMap[r][c] == 2){
                        Map[ rr -1 ][ cc ] ++; // UP
                        Map[ rr + 1 ][ cc ] ++; // DOWN
                    }else if(OMap[r][c] == 3){
                        Map[ rr ][ cc - 1 ] ++; // LEFT
                        Map[ rr ][ cc + 1 ] ++; // RIGHT
                    }else if(OMap[r][c] == 4){
                        Map[ rr -1 ][ cc ] ++; // UP
                        Map[ rr ][ cc + 1 ] ++; // RIGHT
                    }else if(OMap[r][c] == 5){
                        Map[ rr + 1 ][ cc ] ++; // DOWN
                        Map[ rr ][ cc + 1 ] ++; // RIGHT
                    }else if(OMap[r][c] == 6){
                        Map[ rr + 1 ][ cc ] ++; // DOWN
                        Map[ rr ][ cc - 1 ] ++; // LEFT
                    }else if(OMap[r][c] == 7){
                        Map[ rr -1 ][ cc ] ++; //  UP
                        Map[ rr ][ cc - 1 ] ++; // LEFT
                    }
                }
            }
 
            int hole_r = 2 * OHOLE_R + 1;
            int hole_c = 2 * OHOLE_C + 1;
     
            int answer = bfs(hole_r,hole_c);
 
            System.out.println("#" + test + " " + answer);
        }
    }
  
    private static int bfs(int hole_r,int hole_c) {
        LinkedList<int[]> que = new LinkedList<>();
        LinkedList<int[]> que_;
        int count = 0;
        int time = 0;
        que.add(new int[]{hole_r,hole_c});
        visit[hole_r][hole_c] = true;
         
        while(que.size()>0 && time < L) {
            que_ =  new LinkedList<>();
            for(int[] q : que) {
                int r = q[0];
                int c = q[1];
                count ++;
                for(int[] d : dir) {
                    int dr = d[0];
                    int dc = d[1];
                    int rr = r + dr;
                    int cc = c + dc;
                    int gor = r + 2 * dr;
                    int goc = c + 2 * dc;
                     
                    if(!(0 <= gor && gor < RR && 0 <= goc && goc < CC ) || visit[gor][goc])
                        continue;
                    if(Map[rr][cc] == 2) {
                        que_.add(new int[] {gor,goc});
                        visit[gor][goc] = true;
                    }
                }
            }
            que = que_;
            time ++;
        }
        return count;
    }
}