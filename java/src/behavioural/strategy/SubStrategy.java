package behavioural.strategy;

public class SubStrategy implements Strategy {
    static int execute(int firstNum, int secondNum) {
        return firstNum - secondNum;
    }
}
