import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        sc.useDelimiter(":");
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println((a+1) + ":" + b);
        // String s = sc.next();
        // String[] strArr = s.split(":");
        // System.out.println(Integer.parseInt(strArr[0])+1 + ":" + strArr[1]);
    }
}