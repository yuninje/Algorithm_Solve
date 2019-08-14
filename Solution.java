package homework0814;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringBufferInputStream;
import java.util.StringTokenizer;

public class Solution {
    static String [] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for(int t = 1; t<=10; t++){
            int N = Integer.parseInt(br.readLine());
            arr = new String[N+1];

            for(int i = 1; i<N+1; i++){
                st = new StringTokenizer(br.readLine());
                st.nextToken();
                arr[i] = st.nextToken();
            }

            for(int i = N; i>2; i--){
                if( i % 2 == 0) { } // left
                else{  // right
                    // 확인
                    if (checkNum(i)){
                        if(checkNum(i-1)){
                            if(!checkNum(i/2)){
                                int a = Integer.parseInt(arr[i-1]);
                                int b = Integer.parseInt(arr[i]);
                                String oper = arr[i/2];
                                switch (oper){
                                    case "+":
                                        arr[i/2] = "1";
                                        break;
                                    case "-":
                                        arr[i/2] = "1";
                                        break;
                                    case "*":
                                        arr[i/2] = "1";
                                        break;
                                    case "/":
                                        arr[i/2] = "1";
                                        break;
                                }
                                i--;
                            }else{
                                arr[i/2] = "0";
                            }
                        }else{
                            arr[i/2] = "0";
                        }
                    }
                    else{
                        arr[i/2] = "0";
                    }
                }
            }

            System.out.println("#" + t + " " + arr[1]);
        }


    }

    static boolean checkNum(int i){
        for(int s = 0; s<arr[i].length(); s++){
            if(arr[i].charAt(s)-'0' >= 0 && arr[i].charAt(s)-'0' <10){}
            else{
                return false; // 문자
            }
        }
        return true; // 숫자
    }
}
