package 캠핑;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public static void main(String[] args) {
        System.out.println(solution(4, new int[][]{{0,0},{1,1},{0,2},{2,0}}));
    }
    static public int solution(int n, int[][] data) {
        List<int[]> list1 ;
        List<int[]> list2 ;
        List<int[]> list3 ;
        List<int[]> list4;
        int answer = 0;
        boolean breakFlag ;
        for(int i = 0; i<n; i++){
            System.out.println("i : " + i + "=========================================================="+ data[i][0] + " , " + data[i][1]);
            list1 = new ArrayList<>();
            list2 = new ArrayList<>();
            list3 = new ArrayList<>();
            list4 = new ArrayList<>();
            int r = data[i][0];
            int c = data[i][1];
            for(int j = 0; j<n; j++){
                if(i==j)
                    continue;
                System.out.println("j : " + j + "=="+ data[j][0] + " , " + data[j][1]);

                int rr = data[j][0];
                int cc = data[j][1];
                breakFlag = false;
                if(r < rr && c > cc){
                    // 좌상
                    int idx = 0;

                    for(int l = 0; ){
                        int lr = l[0];
                        int lc = l[1];
                        if (rr >= lr && cc <= lc) {
                            list1.remove(idx);
                        }else if (rr < lr && cc > lc){
                            breakFlag = true;
                            break;
                        }
                        idx ++;
                    }
                    if(!breakFlag) {
                        System.out.println("add");
                        list1.add(new int[]{rr, cc});
                    }
                }else if(r < rr && c < cc){
                    // 우상
                    int idx = 0;
                    for(int[] l : list1){
                        int lr = l[0];
                        int lc = l[1];
                        if (rr >= lr && cc >= lc) {
                            list2.remove(idx);
                        }else if(rr < lr && cc < lc) {
                            breakFlag = true;
                            break;
                        }
                        idx ++;
                    }
                    if(!breakFlag) {
                        System.out.println("add");
                        list2.add(new int[]{rr, cc});
                    }
                }else if(r > rr && c > cc){
                    // 좌하
                    int idx = 0;
                    for(int[] l : list1){
                        int lr = l[0];
                        int lc = l[1];
                        if (rr <= lr && cc <= lc) {
                            list3.remove(idx);
                        }else if(rr > lr && cc > lc){
                            breakFlag = true;
                            break;
                        }
                        idx ++;
                    }
                    if(!breakFlag) {
                        System.out.println("add");
                        list3.add(new int[]{rr, cc});
                    }
                }else{
                    // 우하
                    int idx = 0;
                    for(int[] l : list1){
                        int lr = l[0];
                        int lc = l[1];
                        if (rr <= lr && cc >= lc) {
                            list4.remove(idx);
                        }else if(rr > lr || cc < lc) {
                            breakFlag = true;
                            break;
                        }
                        idx ++;
                    }
                    if(!breakFlag) {
                        System.out.println("add");
                        list4.add(new int[]{rr, cc});
                    }
                }
            }
            answer += list1.size();
            answer += list2.size();
            answer += list3.size();
            answer += list4.size();
            System.out.println("answer : " + answer);
        }
        return answer/2;
    }
}