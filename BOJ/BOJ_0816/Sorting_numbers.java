package BOJ_0816;

import java.util.Scanner;

public class Sorting_numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int arr[] = new int[num];

        for(int i=0; i<num; i++){
            arr[i] = sc.nextInt();
        }

        // 버블정렬 구현
        for(int i = 0; i < num - 1; i++){
            for(int j = 0; j < num - 1 - i; j++){
                if(arr[j] > arr[j + 1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        for(int i=0; i<num; i++){
            System.out.println(arr[i]);
        }
    }
}

