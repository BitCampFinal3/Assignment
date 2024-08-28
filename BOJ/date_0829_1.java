import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); 
        int T = sc.nextInt(); 
        int[] score = new int[N]; 

        for (int i = 0; i < N; i++) {
            score[i] = sc.nextInt();
        }

        // 삽입 정렬: 내림차순으로 정렬
        for (int i = 1; i < N; i++) {
            int target = score[i];
            int j = i - 1;

            // 런타임 에러: 'j >= 0' 삽입
            while (j >= 0 && score[j] < target) { 
                score[j + 1] = score[j];
                j = j - 1; 
            }
            score[j + 1] = target;
        }

        System.out.println(score[T - 1]);
    }
}
