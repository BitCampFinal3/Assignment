package boj_study_day2;

import java.util.Scanner;

public class Boj_2750_BubbleSort {

	public static void main(String[] args) {
		
        Scanner sc = new Scanner(System.in);

        // 첫째 줄에서 N을 입력 받음
        int N = sc.nextInt();

        // N개의 수를 저장할 배열을 초기화
        int[] numbers = new int[N];

        // 각 숫자를 배열에 저장
        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }

        // 버블 정렬을 사용하여 오름차순으로 정렬
        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j < N - 1 - i; j++) {
                if (numbers[j] > numbers[j + 1]) {
                    // swap numbers[j] and numbers[j + 1]
                    int temp = numbers[j];
                    numbers[j] = numbers[j + 1];
                    numbers[j + 1] = temp;
                }
            }
        }

        // 정렬된 배열을 출력
        for (int num : numbers) {
            System.out.println(num);
        }
        
        sc.close();

	}

}
