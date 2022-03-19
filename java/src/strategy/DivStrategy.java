package strategy;

public class DivStrategy implements Strategy {
    static int execute(int firstNum, int secondNum) {
        return firstNum / secondNum;
    }
}
