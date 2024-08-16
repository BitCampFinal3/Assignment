import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuffer[] arr = new StringBuffer[3];
        int ans = 0;
        for(int i = 0; i < 3; i++){
            arr[i] = new StringBuffer(sc.nextLine());
            if(arr[i].charAt(0) != 'F' && arr[i].charAt(0) != 'B'){
                ans = Integer.parseInt(arr[i].toString()) + (3 - i);
                break;
            }
        }

        sc.close();

        if(ans % 15 == 0){
            System.out.println("FizzBuzz");
        } else if(ans % 3 == 0){
            System.out.println("Fizz");
        } else if(ans % 5 == 0){
            System.out.println("Buzz");
        } else {
            System.out.println(ans);
        }

    }
}