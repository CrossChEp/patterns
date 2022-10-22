package generating.abstract_factory.factories;

import generating.abstract_factory.products.Chair;
import generating.abstract_factory.products.SimpleChair;
import generating.abstract_factory.products.SimpleSofa;
import generating.abstract_factory.products.Sofa;

public class SimpleFurnitureFactory implements AbstractFurnitureFactory {
    @Override
    public Chair produceChair() {
        return new SimpleChair();
    }

    @Override
    public Sofa produceSofa() {
        return new SimpleSofa();
    }
}
