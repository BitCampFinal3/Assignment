package boj_study.day_1;

import java.util.Scanner;

public class _11720 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 숫자의 개수 입력
		System.out.println("숫자의 개수: ");
		int numCnt = sc.nextInt();
		
		// 숫자 입력
		System.out.println("숫자 입력: ");
		String nums = sc.next();
		sc.close();
		
		// 합계 초기화
		int sum = 0;
		
		for (int i = 0; i < numCnt; i++) {
			// ASCI 값이 더해지는 문제 해결
			sum += Character.getNumericValue(nums.charAt(i));
		}
		System.out.println(sum);
	}

}
