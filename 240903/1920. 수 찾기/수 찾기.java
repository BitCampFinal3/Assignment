import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main{
    static List<Integer> intList = new ArrayList<>();

    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            int n = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int i = 0; i < n; i++){
                intList.add(Integer.parseInt(st.nextToken()));
            }

            Collections.sort(intList);

            n = Integer.parseInt(br.readLine());

//            int num;
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < n; i++){
                bw.write(binarySearch(Integer.parseInt(st.nextToken()), 0, intList.size() - 1) + "\n");
            }

            bw.flush();
            bw.close();

        } catch(Exception e){
            e.printStackTrace();
        }
    }

    public static int binarySearch(int num, int l, int r){
        if(l > r){
            return 0;
        }

        int mid = (l + r) / 2;

        if(intList.get(mid)> num){
            return binarySearch(num, l, mid - 1);
        }

        if(intList.get(mid) < num){
            return binarySearch(num, mid + 1, r);
        }

        if(intList.get(mid) == num){
            return 1;
        }

        return 99;
    }

}