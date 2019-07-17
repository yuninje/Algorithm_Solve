public class 큰_수_만들기 {
    public static String solution(String number, int k, String rightAnswer) {
        int count = 0;
        String answer = number;
        while (k != 0){
            if(count+k+1>answer.length()){
                answer = answer.substring(0,answer.length()-k);
                break;
            }
            int max_position = count;
            int max = answer.charAt(max_position);

            for(int i = count+1; i<k+count+1; i++){

                if(max < answer.charAt(i)){
                    max = answer.charAt(i);
                    max_position = i;
                }
            }
            k = k - (max_position-count);

            answer = answer.substring(0,count)+answer.substring(max_position,answer.length());
            System.out.println("answer : " + answer);
            count += 1;
        }

        System.out.println("number : "+ number + "    answer : " + answer +"         right answer : " + rightAnswer);
        return answer;
    }
}