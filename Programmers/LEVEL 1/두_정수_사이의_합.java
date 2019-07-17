public class 두_정수_사이의_합 {
    public static long solution(int a, int b) {
        long answer;

        long absBig = Math.abs(a) >= Math.abs(b) ? a : b;
        long absSmall = Math.abs(a) >= Math.abs(b) ? b : a;

        long totalAbsBig = getSum(absBig);
        long totalAbsSmall = getSum(absSmall);

        if( absBig * absSmall >=0){      // 부호가 같을때
            answer = totalAbsBig - totalAbsSmall + absSmall;
        }else{                           // 부호가 다를때
            answer = totalAbsBig + totalAbsSmall;
        }

        System.out.println(answer);
        return answer;
    }

    // a 부터 0 까지의 정수를 더하기
    // ex)  getSum(-3) = (-3) + (-2) + (-1) + 0 = -6
    //      getSum(3) = 3 + 2 + 1 + 0 = 6
    public static long getSum(long num){
        long absNum = Math.abs(num);
        long totalAbsNum = absNum * (absNum+1) / 2;
        if(num >= 0)
            return absNum * (absNum+1) / 2;
        else// a < 0
            return ( absNum * (absNum+1) / 2 ) * -1;
    }
}
