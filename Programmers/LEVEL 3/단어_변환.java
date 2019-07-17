class Solution {
    int answer = Integer.MAX_VALUE;
    public int solution(String begin, String target, String[] words) {
        boolean[] useWords = new boolean[words.length];
        dfs(words, target,useWords, begin, 0);
        if(answer == Integer.MAX_VALUE)
            answer = 0;
        return answer;
    }

    void dfs(String[] words, String target, boolean[] useWords, String now, int count){
        boolean[] useNew = new boolean[words.length];
        for(int i = 0; i< words.length; i++)
            useNew[i] = useWords[i];
        if(now.equals(target)){
            answer = answer < count ? answer : count;
        }
        for(int k = 0; k < useNew.length; k++){
            if(useNew[k])
                System.out.print("  T");
            else
                System.out.print("  F");
        }
        System.out.println("");
        System.out.println(now + "  " + (count));

        for(int i = 0; i<words.length; i++){
            //check
            if(!useNew[i]){
                int sameCount = 0;
                for(int j = 0; j<target.length(); j++){
                    if(words[i].charAt(j) == now.charAt(j)){
                        sameCount ++;
                    }
                }
                if(sameCount == target.length()-1){
                    useNew[i] = true;
                    dfs(words, target, useNew, words[i], count+1);
                }
            }
        }
    }
}