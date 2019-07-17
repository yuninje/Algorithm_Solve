import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int t = 1; t<= T; t++) {
            int[] arr = new int[101];
       		int testCase = sc.nextInt();

			for(int i = 0; i<1000; i++) {
				int num = sc.nextInt();
				arr[num]++;
			}
			
			int max_index = 0;
;			int max = 0;
			for(int i = 0; i<101; i++) {
				if(max <= arr[i]) {
					max_index = i;
					max = arr[i];
				}
			}
			System.out.println("#" + t + " " + max_index);
		}
	}
}