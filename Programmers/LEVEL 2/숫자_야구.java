public class 숫자_야구 {
    public int solution(int[][] baseball) {
        int answer = 0;
        boolean[] arr = new boolean[1000];
        // 초기화
        for(int i = 100; i<1000; i++){
            if(i % 10 == 0)
                ;   // _ _ 0
            else if((i / 10)%10  == 0)
                ;   // _ 0 _
            else
                arr[i] = true;
        }

        for(int i = 100; i<1000; i++){
            if(arr[i]){
                int[] num = new int[3];
                num[0] = i / 100;
                num[1] = (i/10)%10;
                num[2] = i % 10;
                if(num[0] == num[1] || num[1] == num[2] || num[0] == num[2]){
                    arr[i] = false;
                    continue;
                }
                for(int j = 0; j<baseball.length; j++){
                    // 체크
                    int strike = 0;
                    int ball = 0;
                    int[] baseNum = new int[3];
                    baseNum[0] = baseball[j][0] / 100;
                    baseNum[1] = (baseball[j][0]/10)%10;
                    baseNum[2] = baseball[j][0] % 10;

                    // check strike, ball
                    for(int k = 0; k<3; k++){
                        if(num[k] == baseNum[k] )
                            strike++;
                        for(int l = 0; l<3; l++){
                            if(l != k && num[k] == baseNum[l])
                                ball++;
                        }
                    }


                    // 다르면 false, break
                    if(strike != baseball[j][1] || ball != baseball[j][2]){
                        arr[i] = false;
                        break;
                    }
                }
            }
        }
        for(int i = 100; i<1000; i++)
            if(arr[i])
                answer++;

        return answer;
    }
}
