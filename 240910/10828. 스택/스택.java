import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try{
            Stack<Integer> stack = new Stack<>();

            int n = Integer.parseInt(br.readLine());

            StringTokenizer st;
            StringBuffer sb;
            int num;

            for(int i = 0; i < n; i++){
                st = new StringTokenizer(br.readLine());
                sb = new StringBuffer(st.nextToken());

                switch (sb.toString()){
                    case "push":
                        num = Integer.parseInt(st.nextToken());
                        stack.push(num);
                        break;
                    case "pop":
                        if(stack.isEmpty()){
                            bw.write("-1\n");
                        } else {
                            bw.write(stack.pop() + "\n");
                        }
                        break;
                    case "size":
                        bw.write(stack.size() + "\n");
                        break;
                    case "empty":
                        bw.write((stack.isEmpty() ? 1 : 0) + "\n");
                        break;
                    case "top":
                        if(stack.isEmpty()){
                            bw.write("-1\n");
                        } else {
                            bw.write(stack.peek() + "\n");
                        }
                        break;
                }
            }

            bw.flush();
            bw.close();
        } catch(Exception e){
            e.printStackTrace();
        }
    }
}