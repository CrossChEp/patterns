package strategy;

public class SumStrategy implements Strategy {
    static int execute(int firstNum, int secondNum) {
        return firstNum + secondNum;
    }
}
