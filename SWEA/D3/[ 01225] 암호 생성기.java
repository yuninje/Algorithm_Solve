import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class amho {
    public static void main(String[] args) throws  Exception{
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for(int t = 0; t<10; t++){
            int test = Integer.parseInt(br.readLine());
            int [] arr = new int[8];
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i<8; i++)
                arr[i] = Integer.parseInt(st.nextToken());
            int idx = 0;
            int count = 1;
            while(true){
                arr[idx] -= count;
                if(arr[idx] <= 0){
                    arr[idx] = 0;
                    break;
                }
                idx = (idx + 1)%8;
                count = count % 5 +1;
            }
            int[] result = new int[8];
            int resultIdx = 0;
            for(int i = idx+1; i<8; i++)
                result[resultIdx++] = arr[i];
            for(int i = 0; i<idx+1; i++)
                result[resultIdx++] = arr[i];

            System.out.print("#"+test+" ");
            for(int i = 0 ; i< 8; i++)
                System.out.print(result[i] + " ");

        }
    }
}
