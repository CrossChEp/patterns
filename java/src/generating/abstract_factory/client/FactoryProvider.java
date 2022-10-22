package generating.abstract_factory.client;

import generating.abstract_factory.factories.AbstractFurnitureFactory;
import generating.abstract_factory.products.Chair;
import generating.abstract_factory.products.Sofa;

public class FactoryProvider {
    private AbstractFurnitureFactory factory;

    public FactoryProvider(AbstractFurnitureFactory factory) {
        this.factory = factory;
    }

    public Chair produceChair() {
        return factory.produceChair();
    }

    public Sofa produceSofa() {
        return factory.produceSofa();
    }
}
