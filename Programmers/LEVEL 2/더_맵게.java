import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;
public class 더_맵게 {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        Arrays.sort(scoville);
        int i = 0;
        int min1 = -1;
        int min2 = -1;
        while(true){
            if(min1 == -1){ // set min1
                if(i < scoville.length){
                    if(!q.isEmpty()){
                        if(scoville[i] >= q.peek()){
                            min1 = q.poll();
                        }else{
                            min1 = scoville[i++];
                        }
                    }else{
                        min1 = scoville[i++];
                    }
                }else{
                    min1 = q.poll();
                }
                if(min1 >= K)
                    break;
            }else{  // set min2
                if(i < scoville.length){
                    if(!q.isEmpty()){
                        if(scoville[i] >= q.peek()){
                            min2 = q.poll();
                        }else{
                            min2 = scoville[i++];
                        }
                    }else{
                        min2 = scoville[i++];
                    }
                }else{
                    if(!q.isEmpty()){
                        min2 = q.poll();
                    }else{
                        return -1;
                    }
                }
                q.offer(min1 + min2 * 2);

                answer++;
                min1 = -1;
            }
        }

        return answer;
    }
}
