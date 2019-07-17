import java.util.Arrays;
import java.util.Comparator;
public class 문자열_내_마음대로_정렬하기 {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        Arrays.sort(strings, new Comparator<String>(){
            @Override
            public int compare(final String a, final String b){
                final String field1 = String.valueOf(a.charAt(n));
                final String field2 = String.valueOf(b.charAt(n));
                if(field1.equals(field2)){
                    return a.compareTo(b);
                }else{
                    return field1.compareTo(field2);
                }
            }
        });
        return strings;
    }
}
