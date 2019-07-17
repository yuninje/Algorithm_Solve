import java.util.Arrays;
public class 나누어_떨어지는_숫자_배열 {
    public int[] solution(int[] arr, int divisor) {
        int[] answer_ = new int[arr.length];
        int answerIndex = 0;
        for(int i = 0; i<arr.length; i++){
            if(arr[i] % divisor == 0){
                answer_[answerIndex] = arr[i];
                answerIndex++;
            }
        }
        int[] answer;
        if(answerIndex == 0)
            answer = new int[]{-1};
        else{
            answer = new int[answerIndex];
            for(int i = 0; i<answerIndex; i++){
                answer[i] = answer_[i];
            }
            Arrays.sort(answer);
        }
        return answer;
    }
}
