public class 문자열_내_p와_y의_개수 {
    boolean solution(String s) {
        int x = 0;
        for(int i = 0; i<s.length() ; i++){
            if(s.charAt(i) == 'y' ||  s.charAt(i) == 'Y')
                x++;
            else if(s.charAt(i) == 'p' || s.charAt(i) == 'P')
                x--;
        }
        if(x == 0)
            return true;
        else
            return false;
    }
}

