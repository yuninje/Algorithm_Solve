// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh
import java.util.Scanner;

public class Ladder {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int test = 1; test<= 10; test++) {
			sc.nextInt();
			int[][] arr = new int[100][102];
			int aimR = 99;
			int aimC = 150;
			
			for(int i = 0; i<100; i++) {
				for(int j = 1; j<=100; j++) {
					arr[i][j] = sc.nextInt();
					if(arr[i][j] == 2) {
						aimC = j;
					}
				}
			}
			while(aimR != 1) {
				aimR--;
				while(arr[aimR][aimC-1] == 1)
					aimC--;
				while(arr[aimR][aimC+1] == 1)
					aimC++;
			}
			
			aimC--;
			
			
			System.out.println("#" + test + " "+aimC);
		}
	}

}
