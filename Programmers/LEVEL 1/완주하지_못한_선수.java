import java.util.Arrays;

public class 완주하지_못한_선수 {
    public static String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        for(int i = 0; i<completion.length;i++){
            if(!participant[i].equals(completion[i])){
                answer = participant[i];
                break;
            }
        }
        if(answer == ""){
            answer = participant[participant.length-1];
        }
        System.out.println(answer);
        return answer;
    }
}
