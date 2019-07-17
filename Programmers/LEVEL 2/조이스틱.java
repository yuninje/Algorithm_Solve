public class 조이스틱 {
    public int solution(String name) {
        int answer = 0;
        int size = name.length();
        int startA = 0;
        int endA = 0;

        // start A
        for(int i = 1 ; i < size; i++){
            if(name.charAt(i) == 'A'){
                startA++;
            }else{
                break;
            }
        }
        // end A
        for(int i =size-1; i>0; i--){
            if(name.charAt(i) == 'A'){
                endA++;
            }else{
                break;
            }
        }
        answer = size -1 - (startA > endA ? startA : endA);

        // middle A
        for(int i = 1, sizeA = 0, start = -1; i < size; i++){
            if(name.charAt(i) == 'A'){
                if(start != -1){
                    sizeA ++;
                }else{
                    start = i;
                    sizeA = 1;
                }
            }else{
                if(start != -1){
                    if(start > size - (start + sizeA)){
                        if(answer > (size-start- sizeA) * 2 + start-1)
                            answer = (size-start- sizeA) * 2 + start-1;
                    }else{
                        if(answer > (size-start- sizeA) + start * 2 - 2){
                            answer = (size-start- sizeA) + start * 2 - 2;
                        }
                    }
                }
                start = -1;
            }
        }

        // 65 : A, 90 : Z
        for(int i = 0; i<size; i++){
            char a = name.charAt(i);
            answer += a-'A'<= 13 ? a-'A' : 26 - (a-'A');
        }

        return answer;
        }
}
