import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static String solution(int n) {
        String answer = "";
        int a = 1;  // + b * 3
        int b = 1;  // * 3

        while (n >= a) {
            if (((n - a) / b) % 3 == 0) {
                answer = 1 + answer;
            } else if (((n - a) / b) % 3 == 1) {
                answer =2 + answer;
            } else {
                answer =4+ answer;
            }
            a = a + b * 3;
            b = b * 3;
        }
        System.out.println(" result : " + answer);
        return answer;
    }
}
