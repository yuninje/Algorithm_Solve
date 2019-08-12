// # https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWwtYmX6hvsDFAWU&
// 1 <= N <= 200,000
// 1 <= S(i) <= N

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 만화책_정렬하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; ++t) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N+1];
            int cnt = 1;
            StringTokenizer st = new StringTokenizer(br.readLine());
            int idx = 0;
            while (st.hasMoreTokens()) {
                arr[Integer.parseInt(st.nextToken())] = idx++;
            }
            for(int i = 2; i<=N; i++){
                if(arr[i-1] > arr[i])
                    cnt++;
            }

            System.out.println("#" + t + " " + cnt);
        }
    }
}
