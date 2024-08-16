package _group3_BOJ;

import java.util.Scanner;

public class date_0816_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();

        // 배열로 숫자 받음
        int[] arr = new int[N];

        // 배열에 저장
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        // 버블 정렬
        int temp = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 1; j < arr.length - i; j++) {
                if (arr[j - 1] > arr[j]) {
                    temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        
        // 디버깅 용도...?
//        System.out.println(Arrays.toString(arr));
        
        for (int i = 0; i < N; i++) {
            System.out.println(arr[i]);
        }
	}
}
