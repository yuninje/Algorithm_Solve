public class 탑 {
    public static int[] solution(int[] heights) {
        int[] answer = new int[heights.length];
        boolean breakFlag = false;
        for (int i = heights.length - 1; i > 0; i--) {  // 송신하는 탑
            breakFlag = false;
            for (int j = i - 1; j >= 0; j--) {       // 수신하는 탑
                if (heights[j] > heights[i]) {
                    answer[i] = j+1;
                    breakFlag = true;
                    break;
                }
            }
            if (!breakFlag) {
                answer[i] = 0;
            }
        }
        System.out.print("answer : {");
        for (int i = 0; i < heights.length; i++) {
            System.out.print("  " + answer[i] + "  ");
        }
        System.out.println("}");
        return answer;
    }
}
