public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        double ft, mi;
        ft = 9.2;
        mi = 1.3;
        System.out.printf("%.1fft = %.1fcm", ft, ftToCm(ft));
        System.out.println();
        System.out.printf("%.1fmi = %.1fcm", mi, miToCm(mi));
    }

    private static double ftToCm(double ft) {
        return ft * 30.48;
    }

    private static double miToCm(double mi) {
        return mi * 160934;
    }
}