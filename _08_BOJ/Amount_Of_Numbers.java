import java.util.Scanner;

public class Amount_Of_Numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        String nums =sc.next();

        int sum = 0;

        for(int i = 0; i < num; i++) {
            sum += nums.charAt(i)-'0';
        }

        System.out.println(sum);
    }
}
