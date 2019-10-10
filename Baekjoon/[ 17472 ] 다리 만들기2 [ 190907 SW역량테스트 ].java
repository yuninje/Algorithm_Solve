package 다리만들기2;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    /*
     1 <= R, C <= 10
     3 <= R * C <= 100
     2 <= 섬 <= 6
     */
    static class Loc{
        int r;
        int c;
        int d; // 방향
        Loc(int r, int c){
            this.r = r;
            this.c = c;
        }
        Loc(int r, int c, int d){
            this.r = r;
            this.c = c;
            this.d = d;
        }
    }

    static class Dist implements Comparable<Dist>{
        int s;
        int e;
        int d;
        Dist(int s, int e, int d){
            this.s = s;
            this.e = e;
            this.d = d;
        }

        @Override
        public int compareTo(Dist dist) {
            return this.d - dist.d;
        }

        @Override
        public String toString() {
            return "[ " + s + " , " + e + " , " + d + " ] ";
        }
    }

    static int R;
    static int C;
    static int[][] map;
    static int[][] adj;
    static boolean[][] visit;
    static int idx;
    static int[][] dir = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    static LinkedList<Dist> dists;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split(" ");
        R = Integer.parseInt(line[0]);
        C = Integer.parseInt(line[1]);
        map = new int[R][C];
        for(int r = 0 ; r<R; r++){
            map[r] = new int[C];
            line = sc.nextLine().split(" ");
            for(int c = 0; c <C; c++){
                map[r][c] = Integer.parseInt(line[c]);
            }
        }
        visit = new boolean[R][C];
        idx = 2;

        // 네이밍
        for(int r = 0; r<R; r++){
            for(int c = 0; c<C; c++){
                if( map[r][c] == 1){
                    naming(r,c,idx++);
                }
            }
        }

        // 거리 구하기

        // adj 배열 초기화
        adj = new int[idx][idx];
        for(int r = 0; r < idx; r++){
            adj[r] = new int[idx];
            for(int c = 0; c < idx; c++){
                adj[r][c] = 10;
            }
        }
        visit = new boolean[R][C];
        for(int r = 0; r < R ; r++){
            for(int c = 0; c < C; c++){
                if(map[r][c] != 0 && ! visit[r][c]){
                    check_dist(r,c,map[r][c]);
                }
            }
        }

        // adj 배열을 ( start, end, distance ) 로 변환
        dists = new LinkedList<>();
        for(int r = 2; r < idx ; r++){
            for(int c = r+1; c < idx; c++){
                if(adj[r][c] == 10) continue;
                dists.add(new Dist(r,c,adj[r][c]));
            }
        }

        dists.sort(Dist::compareTo);

        // 최소 스패닝 트리
        int[] pos = new int[idx];
        for(int i = 0; i<idx; i++)
            pos[i] = -1;

        LinkedList<LinkedList<Integer>> boxes = new LinkedList<>();
        LinkedList<Integer> box;

        int answer = 0;
        for(Dist dist : dists){

            int a = dist.s;
            int b = dist.e;
            int d = dist.d;

            if(pos[a] == -1 && pos[b] == -1){
                // a, b 가 어디에도 속하지 않음
                box = new LinkedList<>();
                box.add(a);
                box.add(b);

                pos[a] = boxes.size();
                pos[b] = boxes.size();

                boxes.add(box);
            }else if(pos[a] == -1 || pos[b] == -1) {
                // 둘 중 하나가 속하지 않음
                int yesG = (pos[a] == -1) ? b : a;
                int noG = (pos[a] == -1) ? a : b;
                boxes.get(pos[yesG]).add(noG);
                pos[noG] = pos[yesG];
            }else{
                // a, b 모두 속함.
                // 같을때
                if(pos[a] == pos[b]){
                    continue;
                }
                // 다를때 병합.
                int sIdx = (pos[a] > pos[b]) ? b : a;
                int bIdx = (pos[a] > pos[b]) ? a : b;
                int sPos = pos[sIdx];
                int bPos = pos[bIdx];

                // bidx 에서 sidx 로 옯김
                for(Integer bo : boxes.get(bPos)){
                    boxes.get(sPos).add(bo);    // 이사 가고
                    pos[bo] = sPos;             // 구청에 신고 하고
                }
                boxes.get(bPos).clear();        // 이전 집 정리
            }

            answer += d;
        }
        if(boxes.size() == 0 || boxes.get(0).size() != idx-2)
            System.out.println("-1");
        else
            System.out.println(answer);
    }
    static void print_map(){
        for(int r = 0; r<R; r++){
            for(int c = 0; c<C; c++){
                System.out.print(map[r][c] + " " );
            }
            System.out.println();
        }
        System.out.println();
    }

    static void print_adj(){
        for(int r = 2; r<idx; r++){
            for(int c = 2; c<idx; c++){
                System.out.print(adj[r][c] + " " );
            }
            System.out.println();
        }
        System.out.println();
    }
    static void naming(int r, int c, int idx){
        visit[r][c] = true;
        map[r][c] = idx;
        for(int[] d : dir){
            int rr = r + d[0];
            int cc = c + d[1];
            if(0 <= rr && rr < R && 0 <= cc && cc < C && map[rr][cc] == 1){
                naming(rr,cc,idx);
            }
        }
    }

    static void check_dist(int r,int c, int name){
        visit[r][c] = true;
        Queue<Loc> que ; // 현재 레벨 큐
        Queue<Loc> que_; // 다음 레벨 큐

        LinkedList<Loc> group = new LinkedList<>(); // name 집합

        que = new LinkedList<>();
        que.add(new Loc(r,c));

        while(! que.isEmpty()){
            que_ = new LinkedList<>();
            for(Loc l : que){
                group.add(l);
                for(int[] d : dir){
                    int rr = l.r + d[0];
                    int cc = l.c + d[1];

                    if(0 <= rr && rr < R && 0 <= cc && cc < C && map[rr][cc] == name && ! visit[rr][cc]){
                        visit[rr][cc] = true;
                        que_.add(new Loc(rr,cc));
                    }
                }
            }
            que = que_;
        }


        que = new LinkedList<>();
        for(Loc l : group){
            for(int d = 0; d < 4; d++){
                que.add(new Loc(l.r, l.c, d));
            }
        }

        // ======현재 섬부터 다른 섬까지의 거리 구하기=========================
        int distance = 0;
        while (! que.isEmpty()){
            que_ = new LinkedList<>();

            for(Loc l : que){
                int rr = l.r + dir[l.d][0];
                int cc = l.c + dir[l.d][1];

                if(0 <= rr && rr < R && 0 <= cc && cc < C ) {
                    if (map[rr][cc] == name)
                        continue;
                    else if (map[rr][cc] == 0) {
                        l.r = rr;
                        l.c = cc;
                        que_.add(l);
                    } else {  // 다른 섬 발견
                        if(distance < 2) continue;
                        if (adj[name][map[rr][cc]] == 10)
                            adj[name][map[rr][cc]] = distance;
                    }
                }
            }
            que = que_;
            distance ++;
        }

    }
}
