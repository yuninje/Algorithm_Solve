import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 모의고사 {
    public static int[] solution(int[] answers) {
        List<Integer> answerList = new ArrayList<>();
        int[] person1 = {1,2,3,4,5};
        int[] person2 = {2,1,2,3,2,4,2,5};
        int[] person3 = {3,3,1,1,2,2,4,4,5,5};
        int[][] persons = {person1, person2, person3};
        int[] elementCount = {5,8,10};
        int[] scores = {0,0,0};

        for(int i = 0; i<answers.length; i++){
            for(int j = 0; j < persons.length; j++){
                if(persons[j][i % elementCount[j]] == answers[i])
                    scores[j] ++;
            }
        }

        for(int score : scores)
            System.out.print ( score + "  " );
        System.out.println();

        int max = scores[0];
        answerList.add(1);
        for(int i = 1;i<scores.length; i++){
            if(max == scores[i]) {
                answerList.add(i+1);
            }
            else if(max < scores[i]) {
                answerList = new ArrayList<>();
                answerList.add(i+1);
                max = scores[i];
            }
        }

        System.out.println(answerList);

        int [] answer = new int[answerList.size()];
        int size = 0;
        for(int temp : answerList) {
            answer[size++] = temp;
        }

        return answer;
    }
}
