package BOJ_0821;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Sort_Word {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());

        String[] strArr = new String[num];

        for(int i = 0; i < num; i++) {
            strArr[i] = br.readLine();
        }

        Arrays.sort(strArr, new Comparator<String>() {
            public int compare(String s1, String s2) {
                // 단어 길이가 같은 경우
                if(s1.length() == s2.length()) {
                    return s1.compareTo(s2);
                } else {
                    return s1.length() - s2.length();
                }
            }
        });

        StringBuilder sb = new StringBuilder();

        sb.append(strArr[0]).append('\n');

        for(int i = 1; i < num;  i++) {
            // 중복되지 않는 출력
            if(!strArr[i].equals(strArr[i - 1])) {
                sb.append(strArr[i]).append('\n');
            }
        }
        System.out.println(sb);
    }
}
