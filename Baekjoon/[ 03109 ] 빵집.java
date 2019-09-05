class Main{
    static int[][] dir = new int[][]{{-1,1},{0,1},{1,1}};
    static char[][] arr;
    static boolean flag;
    static int answer;
    static int R;
    static int C;

    public static void main(String[] args){
        BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
		String [] str = br.readLine().split(" ");
		
		R = Integer.parseInt(str[0]);
		C = Integer.parseInt(str[1]);
		arr = new char[R][C];
        for (int i = 0; i < R; i++)
			arr[i] = br.readLine().toCharArray();
        System.out.println(answer);
    }
    static void dfs(int r, int c){
        if(c == C-1){
            answer ++;
            flag = true;
            return;
        }

        for(int[] d : dir){
            int rr = r + d[0];
            int cc = c + d[1];
            if(R > rr && rr >= 0 && C > cc && cc >= 0 && arr[rr][cc] == '.'){
                arr[rr][cc] = 'x';
                dfs(rr,cc);
                if(flag)
                    return;
            }
        }
    }
}