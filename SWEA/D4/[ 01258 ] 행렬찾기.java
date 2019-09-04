package 행렬찾기;

import java.util.*;

class Solution{
    static int N;
    static int[][] arr;
    static int[][] dir = new int[][]{{0,1},{1,0}};
    static int[] min;
    static int[] max = new int[]{0,0};
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        List<int[]> list;
        int T = sc.nextInt();
        sc.nextLine();
        for(int test = 1; test<= T; test++){
            N = sc.nextInt();
            sc.nextLine();
            arr = new int[N][N];
            for(int i = 0; i<N; i++){
                String[] line = sc.nextLine().split(" ");
                for(int j = 0; j<N; j++)
                    arr[i][j] = Integer.parseInt(line[j]);
            }
            list = new ArrayList<>();

            int answer = 0;
            for(int r = 0; r<N; r++){
                for(int c = 0; c<N;c++){
                    if (arr[r][c] == 0)
                        continue;
                    min = new int[]{r,c};
                    max = new int[]{0,0};
                    dfs(r,c);
                    list.add(new int[]{max[1]-min[1]+1, max[0]-min[0]+1});
                }
            }
            Collections.sort(list, new Comparator<int[]>() {
                @Override
                public int compare(int[] i1, int[] i2) {
                    if(i1[0] * i1[1] > i2[0] * i2[1])
                        return 1;
                    else if (i1[0] * i1[1] < i2[0] * i2[1])
                        return -1;
                    else{
                        if (i1[1] > i2[1])
                            return 1;
                        else
                            return -1;
                    }
                }
            });
            StringBuilder sb = new StringBuilder();
            sb.append("#"+test+" "+list.size()+" ");
            for(int[] l : list)
                sb.append(l[1] + " " + l[0] + " ");
            System.out.println(sb);
        }
    }

    static void dfs(int r,int c){
        if(max[0] < r || max[1] < c)
            max = new int[]{r,c};
        arr[r][c] = 0;
        for(int[] d : dir){
            int rr = r + d[0];
            int cc = c + d[1];
            if(N > rr && rr >= 0 && N > cc && cc >= 0 && arr[rr][cc] != 0)
                dfs(rr,cc);
        }
    }
}
