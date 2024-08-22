package boj_study_day3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class _1181 {
	
	// 버퍼 에러를 방지하고자 예외 처리를 날려줘야 함
	public static void main(String[] args) throws IOException {
		
		// 버퍼 호출
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 단어의 개수 N 정의
		int N = Integer.parseInt(br.readLine());
		
		// N개의 문자가 들어갈 빈 문자열 정의
		String[] strArr = new String[N];
		
		// 빈 문자열에 N개 만큼 단어 넣기
		for (int i = 0; i < N; i++) {
			strArr[i] = br.readLine();
		}
		
		// 조건1) 사전 순으로 정렬(Arrays.sort 활용)
		// 조건2) 단어의 길이 순으로 정렬
		Arrays.sort(strArr, new Comparator<String>() {
			public int compare(String s1, String s2) {
				// 조건2-1) 단어의 길이가 같을 때 
				if (s1.length() == s2.length()) {
					return s1.compareTo(s2);
				} 
				// 조건2-2) 단어의 길이가 다를 때
				else {
					return s1.length() - s2.length();
				}
			}
		});
		
		// 빌더 호출
		StringBuilder sb = new StringBuilder();
		 
		// 문자열에 공백 제거
		sb.append(strArr[0]).append('\n');
		
		// 조건3) 중복되는 단어는 하나만 출력
		for (int i = 1; i < N; i++) {
			if (!strArr[i].equals(strArr[i - 1])) {
				sb.append(strArr[i]).append('\n');
			}
		}
		
		System.out.println(sb);
		
		
	}

}
