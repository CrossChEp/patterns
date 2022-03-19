package strategy;

import java.util.NoSuchElementException;

public interface Strategy {
    static int execute(int firstNum, int secondNum) {
        System.out.println("No!");
        return 0;
    }
}
