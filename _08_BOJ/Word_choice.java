import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Word_choice {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        String[] strArr = new String[num];

        sc.nextLine();

        for(int i = 0; i < num; i++) {
            strArr[i] = sc.nextLine();
        }

        // 정렬
        // Comparator 는 객체를 비교할 수 있도록 해주는 인터페이스
        // 정렬할 배열 타입을 String 으로.
        Arrays.sort(strArr, new Comparator<String>() {
            public int compare(String a1, String a2) {
                // 단어 길이가 같은 경우 사전순으로 정렬해주기
                if(a1.length() == a2.length()) {
                    return a1.compareTo(a2);
                }
                // 아님말고
                return a1.length() - a2.length();

                // 이것이 가능한 이유.
                // {7,3,5} 배열
                // public int compare(int a1, int a2) / {return a1 - a2} 를 예시로 보자.
                // 맨 처음 a1 = 7, a2 = 3.
                // 즉 7-3 = 4. 4는 양수이므로, a1과 a2의 위치가 바뀌게 된다.
                // 그럼 {3,7,5}가 되고 a1 = 7, a2 = 5 가 되면서 다시 양수가 반환되고 위치가 변경.
                // 따라서 {3,5,7} 배열로 순서대로 완성.
                // Compare 메소드는 반환값에 의해 우선순위를 판단하고, 위치를 변경하거나 그대로 두는 역할.
            }
        });

        System.out.println(strArr[0]);

        for(int i = 1; i < num; i++) {
            // 중복이 아닌경우 표출
            if(!strArr[i].equals(strArr[i-1])) {
                System.out.println(strArr[i]);
            }
        }
    }
}
