import java.util.*;

public class Main{
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.nextLine();
		
		StringBuffer sb = new StringBuffer(sc.nextLine());
		
		int sum = 0;
		
		for(int i = 0; i < n; i++) {
			sum += sb.charAt(i) - '0';
		}
		
		System.out.println(sum);
		sc.close();
	}
}