import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for(int test = 1; test<T+1; test++){
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            st = new StringTokenizer(br.readLine());
            for(int n = 0; n<N; n++)
                arr[n] = Integer.parseInt(st.nextToken());

            int[] dp = new int[N];
            int max = 0;
            int answer = 1;
            for(int n = 0; n<N; n++){
                max = 0;
                for(int m = 0; m<n; m++){
                    if(arr[m] <arr[n])
                        max = Math.max(dp[m], max);
                }
                dp[n] = max +1;
                answer = Math.max(answer, max+1);
            }
            System.out.println("#"+test+" " + (answer));
        }

    }
}
