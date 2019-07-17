import java.util.ArrayList;
import java.util.List;

public class 같은_숫자는_싫어 {
    public static int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        int last = -1;
        for(int i : arr){
            if(i != last){
                list.add(i);
                last = i;
            }
        }

        int[] answer = new int[list.size()];
        for(int i = 0; i<list.size(); i++){
            answer[i] = list.get(i);
        }

        System.out.println(answer);
        return answer;
    }
}
