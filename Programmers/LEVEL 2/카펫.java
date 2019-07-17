public class 카펫 {
    public int[] solution(int brown, int red) {
        int [] answer = new int[2];
        // x + y = (brown + 4 ) / 2
        // xy = brown + red
        int xy = brown + red;
        for(int i = xy; i>=1; i--)
            if(xy % i == 0)
                if(i + xy/i == (brown + 4) /2)
                    return new int[]{i , xy/i};
        return answer;
    }
}
