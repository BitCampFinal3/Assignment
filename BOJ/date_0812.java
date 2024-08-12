package _group3_BOJ;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class date_0812 {
	public static void main(String[] args) {
		    // 1. 숫자의 합
		    Scanner sc = new Scanner(System.in);

	        int N1 = sc.nextInt();
	        String num = sc.next();

	        int sum = 0;
 
	        // i < N (?)
	        for (int i = 0; i < N1; i++) {
	            sum += num.charAt(i) - '0'; // 문자를 숫자로 변환 ('0'을 빼면 해당 숫자가 됨)
	        }

	        System.out.println(sum);
	        
	        // --------------------------------------------------------------------------
	        // 2.단어 정렬
	        int N2 = sc.nextInt();
	        sc.nextLine();

	        Set<String> word = new HashSet<>(); // 중복제거
	        
	        // 못 품...

	        sc.close();
	}
}
