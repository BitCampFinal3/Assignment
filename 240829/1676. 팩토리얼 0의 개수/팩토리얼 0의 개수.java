import java.io.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            int n = Integer.parseInt(br.readLine());
            br.close();

            int count = 0;
            for (int i = 5; i <= n; i *= 5) {
                count += n / i;
            }

            bw.write(String.valueOf(count));
            bw.flush();
            bw.close();

        } catch(IOException io){
            io.printStackTrace();
        }

    }

}