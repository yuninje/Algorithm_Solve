package SWEA_03813_그래도_수명이_절반이_되어서는;

import java.util.*;

public class Solution {
    /*
       N 개의 블록 ( 1 ~ N )
       1 <= K <= N <= 200,000
       1 <= W[i] <= 200,000   값이 클수록 남은 수명이 짧다.

       초기 데이터 : K개 덩어리

       i번째 덩어리는 S[i] 개의 연속된 블록에 저장
        작은 번호의 블록부터 저장되어야함.
        하나의 덩어리가 저장된 블록에는 다른 덩어리를 저장할 수 없다.


        */
    static int answer;
    static int N;
    static int K;
    static int[] W;
    static int[] S;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for(int test = 1; test< T+1; test++){
            String[] line = sc.nextLine().split(" ");
            N = Integer.parseInt(line[0]);
            K = Integer.parseInt(line[1]);
            line = sc.nextLine().split(" ");
            W = new int[N];
            for(int i = 0; i<N; i++)
                W[i] = Integer.parseInt(line[i]);
            line = sc.nextLine().split(" ");
            S = new int[K];
            for (int i = 0; i<K; i++)
                S[i] = Integer.parseInt(line[i]);

            // HashMap 을 이용
            HashMap<Integer, ArrayList<Integer>> hashMap = new HashMap<>();
            for(int i = 0; i < N ; i++){
                if(hashMap.containsKey(W[i])){
                    hashMap.get(W[i]).add(i);
                }else{
                    ArrayList<Integer> arrayList = new ArrayList<>();
                    arrayList.add(i);
                    hashMap.put(W[i], arrayList)
                }
            }

            // hashMap 정렬

            // Binary Search 로 탐색
            // 가능하면 start = mid +1
            // 불가능하면 end = mid -1




            // answer = group[start - 1]

            System.out.println("#" + test + " " + answer);
        }
    }
}
