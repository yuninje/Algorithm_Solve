package Level2;

public class 타겟_넘버 {
    public int solution(int[] numbers, int target) {
        return fun(numbers, 0,target, 0);
    }

    int fun(int[] numbers, int value, int target, int count){
        if(count == numbers.length){
            if(value == target)
                return 1;
            else
                return 0;
        }
        return fun(numbers, value + numbers[count], target,count+1) + fun(numbers, value - numbers[count], target, count +1);

    }
}
