import java.util.ArrayList;
import java.util.List;

public class 소수의_합 {
    public static String solution(int n) {
        String answer = "";
        List<Integer> list = new ArrayList<>();
        int total = 0;
        boolean breakFlag = false;

        list.add(2);
        total = total + 2;

        for(int i = 3; i<=n ; i++){
            breakFlag = false;
            for(int num : list){
                if(i % num == 0){
                    breakFlag = true;
                    break;
                }
            }
            if(!breakFlag){
                list.add(i);
                total = total + i;
            }
        }

        answer = list + "=" + total;
        return answer;
    }
}
