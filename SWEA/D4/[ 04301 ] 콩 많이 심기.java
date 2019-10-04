package com.ssafy.step1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_D4_4301_콩많이심기 {
	static int T, R, C, sr, sc, Answer;

	public static void main(String[] args) throws Exception{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(in.readLine());
		for(int t=1; t<=T; ++t) {
//			Answer=0;
			StringTokenizer st = new StringTokenizer(in.readLine()," ");
			C=Integer.parseInt(st.nextToken());
			R=Integer.parseInt(st.nextToken());
			sr = R%4;
			sc = C%4;
			
			Answer=(R-sr)*(C-sc)/2;
			Answer+=sc*(R-sr)/2 + sr*(C-sc)/2;
			
			for(int r=0; r<sr; ++r) {
				for(int c=0; c<sc; ++c) {
					if(r%4<2 && c%4<2) Answer++;
					if(r%4>1 && c%4>1) Answer++;
				}
			}
			
			System.out.println("#"+t+" "+Answer);
		}
	}
}
