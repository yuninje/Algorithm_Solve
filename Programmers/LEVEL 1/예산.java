import java.util.Arrays;

public class 예산 {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int total = 0;
        Arrays.sort(d);

        for(int i : d){
            total += i;
            answer ++;
            if(total > budget){
                answer --;
                break;
            }
        }
        return answer;
    }
}
