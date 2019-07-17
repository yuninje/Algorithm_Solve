import java.util.ArrayList;
import java.util.List;

public class 소수_찾기 {
    public static int solution(int n) {
        int answer = 0;
        List<Integer> list = new ArrayList<>();
        boolean breakFlag = false;

        list.add(2);
        for (int i = 3; i <= n; i++) {
            breakFlag = false;
            for (int num : list) {
                if (i % num == 0) {
                    breakFlag = true;
                    break;
                }
            }
            if (!breakFlag) {
                list.add(i);
            }
        }
        System.out.println(list.size());
        return list.size();
    }
}
