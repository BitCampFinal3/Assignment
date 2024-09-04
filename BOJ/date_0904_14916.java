import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // 거스름돈 액수

        int fiveCent = n / 5; // 사용할 수 있는 5원의 개수
        int remain = n % 5; // 위를 사용하고 나머지 

        if (remain == 0) {  // 5로 나누어 떨어질 떄
            System.out.println(fiveCent);
        } else if (remain == 1 || remain == 3) {  // 나머지가 홀수일 때, -(5원 개수), 2원 사용
            if (fiveCent >= 1) {
                System.out.println(fiveCent - 1 + (remain + 5) / 2);
            } else { // 거슬러 줄 수 없는 경우 (ex. 3원)
                System.out.println(-1);
            }
        } else {
            System.out.println(fiveCent + remain / 2); // 나머지가 짝수 일 때, 2원사용
        }
    }
}
