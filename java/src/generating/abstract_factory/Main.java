package generating.abstract_factory;

import generating.abstract_factory.client.FactoryProvider;
import generating.abstract_factory.factories.SuperDuperFurnitureFactory;
import generating.abstract_factory.products.Chair;

public class Main {
    public static void main(String[] args) {
        SuperDuperFurnitureFactory superDuperFactory = new SuperDuperFurnitureFactory();
        FactoryProvider factory = new FactoryProvider(superDuperFactory);
        Chair chair = factory.produceChair();
        System.out.println(chair.getName());
    }
}
