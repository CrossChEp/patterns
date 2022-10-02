package behavioural.strategy;

import java.util.Scanner;

public class Client {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String command = scanner.next();
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int result = 0;
        switch (command) {
            case "sum":
                SumStrategy sumStrategy = new SumStrategy();
                result = sumStrategy.execute(num1, num2);
                System.out.println(result);
                break;
            case "sub":
                SubStrategy subStrategy = new SubStrategy();
                result = subStrategy.execute(num1, num2);
                System.out.println(result);
                break;
            case "mul":
                MulStrategy mulStrategy = new MulStrategy();
                result = mulStrategy.execute(num1, num2);
                System.out.println(result);
                break;
            case "div":
                DivStrategy divStrategy = new DivStrategy();
                result = divStrategy.execute(num1, num2);
                System.out.println(result);
                break;
            default:
                System.out.println("No such command");
                break;
        }
    }
}
