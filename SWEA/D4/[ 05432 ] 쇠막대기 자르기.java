import java.util.Scanner;
import java.io.FileInputStream;
class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        sc.nextLine();
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int answer = 0;
            int stack = 0;
            String arrangement = sc.nextLine();
            arrangement = arrangement.replace("()","*");
            for(int i = 0; i<arrangement.length()-1; i++){
                if(arrangement.charAt(i) == '(' ){
                    stack++;
                    answer++;
                }else if(arrangement.charAt(i) == '*'){
                    answer = answer + stack;
                }else{ 
                    stack--;
                }
            }
            System.out.println("#" + test_case + " " + answer);
        }
    }
}