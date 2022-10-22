package generating.abstract_factory.factories;

import generating.abstract_factory.products.Chair;
import generating.abstract_factory.products.Sofa;
import generating.abstract_factory.products.SuperDuperChair;
import generating.abstract_factory.products.SuperDuperSofa;

public class SuperDuperFurnitureFactory implements AbstractFurnitureFactory {
    @Override
    public Sofa produceSofa() {
        return new SuperDuperSofa();
    }

    @Override
    public Chair produceChair() {
        return new SuperDuperChair();
    }
}
