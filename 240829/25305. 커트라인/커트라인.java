import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n, k;

        n = sc.nextInt();
        k = sc.nextInt();

        int[] score = new int[n];

        for(int i = 0; i < n; i++){
            score[i] = sc.nextInt();
        }

        sc.close();

        // 삽입정렬
        // 큰 순서 대로
        int max, temp;
        for(int i = 0; i < n - 1; i++){
            max = i;
            for(int j = i + 1; j < n; j++){
                if(score[max] < score[j]){
                    max = j;
                }
            }

            if(max != i){
                temp = score[i];
                score[i] = score[max];
                score[max] = temp;
            }
        }

        System.out.println(score[k - 1]);
        
    }
}