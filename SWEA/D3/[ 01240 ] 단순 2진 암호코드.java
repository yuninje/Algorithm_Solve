package workshop0816;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] amho = {"0001101", "0011001", "0010011","0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for(int test = 1; test <= T; test++){
            StringBuilder sb = new StringBuilder();
            st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
            String [] arr = new String[R];
            boolean flag = false;
            int findC = 0;
            int findR = 0;

            for(int r = 0; r<R; r++){
                arr[r] = br.readLine();
                if(findC == 0 && findR == 0){
                    for(int c = C-1; c>=0; c--){
                        if(arr[r].charAt(c) == '1'){
                            findC = c-55;
                            findR = r;
                            break;
                        }
                    }
                }
            }
            for(int c = findC; c<C; c++){
                for(int i = 0; i<10; i++){
                    boolean breakFlag = false;
                    for(int idx = 0; idx<7; idx++){
                        if(c+idx >= C){
                            breakFlag = true;
                            break;
                        }
                        if(amho[i].charAt(idx) != arr[findR].charAt(c+idx)){
                            breakFlag = true;
                            break;
                        }
                    }

                    if(!breakFlag){
                        sb.append(String.valueOf(i));
                        c += 6;
                        break;
                    }
                }
            }
            System.out.println("sb : " + sb.toString());
            int total = 0;
            int answer = 0;
            for(int i = 0; i<sb.length(); i++){
                answer += sb.charAt(i)-'0';
                if( i % 2 == 0)
                    total += 3 * (sb.charAt(i)-'0');
                else
                    total += (sb.charAt(i)-'0');
            }
            if(total % 10 == 0)
                System.out.println("#"+test+" "+answer);
            else{
                answer = 0;
                System.out.println("#"+test+" "+answer);
            }
        }
    }
}
