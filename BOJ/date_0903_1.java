import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        Arrays.sort(A);

        
        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            int target = sc.nextInt();
            // 이분 탐색
            if (binarySearch(A, target)) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }

    // GPT 도움
    // 이분 탐색 함수
    public static boolean binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == target) {
                return true;  // target이 배열에 존재
            } else if (arr[mid] < target) {
                left = mid + 1;  // 오른쪽 부분 탐색
            } else {
                right = mid - 1;  // 왼쪽 부분 탐색
            }
        }

        return false;  // target이 배열에 존재하지 않음
    }
}
