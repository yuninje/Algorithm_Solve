package swea_03378_스타일리쉬_들여쓰기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int test = 1; test <= T; ++test) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            int r1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            String[] arr1 = new String[r1];
            String[] arr2 = new String[r2];
            for(int r = 0; r<r1; r++)
            	arr1[r] = br.readLine();
            for(int r = 0; r<r2; r++)
            	arr2[r] = br.readLine();
            
            int sc = 0, mc = 0, bc = 0, dot = 0;
            List<int[]> record = new ArrayList();
            for(String ar : arr1) {
            	dot = 0;
            	boolean flag = true;
            	for(int i = 0; i < ar.length(); i++) {
            		char a = ar.charAt(i);
            		if(a == '.' && flag) {
            			dot ++;
            		}else {
            			if(flag) {
            				flag = false;
            				record.add(new int[] {sc,mc,bc,dot});
            			}
            			if(a == '(') sc ++;
            			else if (a == ')') sc --;
            			else if (a == '{') mc ++;
            			else if (a == '}') mc --;
            			else if (a == '[') bc ++;
            			else if (a == ']') bc --;
            		}
            	}
            }
            List<int[]> smb = new ArrayList();
            for(int sv = 1; sv<21; sv++) {
            	for(int mv = 1; mv<21; mv++) {
            		for(int bv = 1; bv<21; bv++) {
            			boolean breakFlag = false;
            			for(int[] rec : record) {
            				sc = rec[0];
            				mc = rec[1];
            				bc = rec[2];
            				dot = rec[3];
            				if(sv * sc + mv * mc + bc * bv != dot) {
            					breakFlag = true;
            					break;
            				}
            			}
            			if(!breakFlag)
            				smb.add(new int[]{sv,mv,bv});
            		}
            	}
            }
            
            sc = 0;
            mc = 0;
            bc = 0;
            int[] answer = new int[r2];
            for(int r = 0; r<r2; r++) {
            	boolean breakFlag = false;
            	int before = -2;
            	for(int[] sm : smb) {
            		int sv = sm[0];
            		int mv = sm[1];
            		int bv = sm[2];
            		
            		dot = sv * sc + mv * mc + bv * bc;
            		
            		if(before != -2) {
            			if(dot != before) {
            				answer[r] = -1;
            				breakFlag = true;
            				break;
            			}
            		}
            		before = dot;
            	}
            	if(!breakFlag)
            		answer[r] = dot;
            	
            	for(int i = 0; i<arr2[r].length(); i++) {
            		char a = arr2[r].charAt(i);
            		if(a == '(') sc ++;
        			else if (a == ')') sc --;
        			else if (a == '{') mc ++;
        			else if (a == '}') mc --;
        			else if (a == '[') bc ++;
        			else if (a == ']') bc --;
            	}
            }
            System.out.print("#"+test+" ");
            for(int a : answer)
            	System.out.print(a+" ");
            System.out.println();
        }
	}

}
