class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] arr = new boolean[n];
        for(int i = 0; i < n; i++){
            if(!arr[i]){
                fun(computers, n, arr, i);
                answer++;
            }
        }

        return answer;
    }

    void fun(int [][]computers,int n,boolean[] arr, int nowPos){
        arr[nowPos] = true;

        for( int i = 0; i<n; i++){
            if( i != nowPos && computers[nowPos][i] == 1){
                if(!arr[i]){
                    fun(computers, n, arr, i);
                }
            }
        }
    }
}