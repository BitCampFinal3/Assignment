import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            int n = Integer.parseInt(br.readLine());
            br.close();

            if(n < 5 && n % 2 == 1){
                bw.write(String.valueOf(-1));
            } else if((n % 5) % 2 == 0){
                bw.write(String.valueOf(n / 5 + (n % 5) / 2));
            } else {
                bw.write(String.valueOf((n / 5 - 1) + ((n % 5) + 5) / 2));
            }

            bw.flush();
            bw.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}