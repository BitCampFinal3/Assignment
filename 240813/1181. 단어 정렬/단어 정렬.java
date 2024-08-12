import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.Set;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Set<String> wordsSet = new HashSet<String>();
		Map<Integer, List<String>> wordsMap = new HashMap<Integer, List<String>>();
		
		int n = sc.nextInt();
		sc.nextLine();
		
		// List를 만든 후 순서대로 정렬(중복제거를 위해 set으로 받은 후 list로 변환)
		for(int i = 0; i < n; i++) {
			String sb = sc.nextLine();
			wordsSet.add(sb);
		}
		
		List<String> words = new LinkedList<String>(wordsSet);
		
		Collections.sort(words);
		
		// 길이를 key로 가진 map으로 변환
		for(int i = 0; i < words.size(); i++) {
			if(wordsMap.isEmpty() || !wordsMap.containsKey(words.get(i).length())) {
				wordsMap.put(words.get(i).length(), new LinkedList<String>());
			} 
			wordsMap.get(words.get(i).length()).add(words.get(i));
		}
		
		List<Map.Entry<Integer, List<String>>> entryList = new LinkedList<>(wordsMap.entrySet());
		// 정렬이 의미가 있는지는 모르겠다. 그래도 혹시 모르니까
		entryList.sort((o1,  o2) -> o1.getKey() - o2.getKey());
		
		for(Entry<Integer, List<String>> entry : entryList) {
			for(String sb : entry.getValue()) {
				System.out.println(sb);
			}
		}	
		sc.close();
	}
	
	

}
