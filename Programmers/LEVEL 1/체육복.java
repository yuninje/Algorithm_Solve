import java.util.Arrays;
public class 체육복 {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int z = 0;
        int x = 0;
        Arrays.sort(lost);
        Arrays.sort(reserve);

        for (int i = 0; i < lost.length; i++) {
            for (int j = z; j < reserve.length; j++) {
                if (lost[i] == reserve[j]) {
                    z = ++j;
                    x--;
                    break;
                }
                if (lost[i] - 1 == reserve[j] || lost[i] + 1 == reserve[j]) {
                    z = ++j;
                    x++;
                    break;
                }
            }
        }
        answer = n - lost.length + x;
        return answer;
    }
}
