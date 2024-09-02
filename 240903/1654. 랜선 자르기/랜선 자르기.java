import java.io.*;
import java.util.*;

public class Main{
    static List<Long> longList = new ArrayList<>();

    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            long n = Long.parseLong(st.nextToken());

            for(int i = 0; i < k; i++){
                longList.add(Long.parseLong(br.readLine()));
            }

            Collections.sort(longList, Comparator.reverseOrder());

            bw.write(String.valueOf(binarySearch(n, 1L, longList.get(0), 0L)));
            bw.flush();
            bw.close();

        } catch(Exception e){
            e.printStackTrace();
        }
    }

    public static long binarySearch(long num, long l, long r, long len){

//        System.out.println("l: " + l + "\t r:" + r + "\tlen: " + len);
        if(l > r){
            return len;
        }

        long mid = (l + r) / 2;

        long cnt = 0;

        for(int i = 0; i < longList.size(); i++){
            cnt += longList.get(i) / mid;
        }

//        System.out.println("cnt: " + cnt);

        if(cnt >= num){
            if(len == 0 || len < mid){
                return binarySearch(num, mid + 1, r, mid);
            }
            return binarySearch(num, mid + 1, r, len);
        } else {
            return binarySearch(num, l, mid - 1, len);
        }
    }

}