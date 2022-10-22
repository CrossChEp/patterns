package generating.abstract_factory.factories;

import generating.abstract_factory.products.Chair;
import generating.abstract_factory.products.Sofa;

public interface AbstractFurnitureFactory {
    Chair produceChair();

    Sofa produceSofa();
}
