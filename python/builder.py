""" This module represents a 'builder' pattern """

from typing import Any


class AbstractCar:
    """abstract class of car

    :functions:
        add
            adds part to car
        list_parts
            prints all parts of the car
    """
    def __init__(self):
        self._parts = []

    def add(self, part: Any):
        self._parts.append(part)

    def list_parts(self):
        print(f'Parts: {self._parts}')


class Car(AbstractCar):
    """It makes sense to use the Builder pattern
    only when your products are quite complex and require extensive configuration.

    Unlike other generative patterns, various concrete builders
    may produce unrelated products. In other words, the results
    different builders may not always follow the same interface
    """
    pass


class SuperCar(AbstractCar):
    pass


class Builder:
    """The Builder interface declares creating
    methods for various parts of Product objects.
    """

    def car(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def produce_engine(self):
        raise NotImplementedError

    def produce_corpus(self):
        raise NotImplementedError

    def produce_sport_engine(self):
        raise NotImplementedError

    def produce_sport_corpus(self):
        raise NotImplementedError


class CarBuilder(Builder):
    """The Builder-specific classes follow the Builder interface and provide
    specific implementations of the construction steps. Your program may have several
    variants of Builders implemented in different ways.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self._car = Car()

    def car(self):
        """Specific Builders should provide their own methods
        getting results. This is due to the fact that different types of builders
        they can create completely different products with different interfaces.
        Therefore, such methods cannot be declared in the base interface.
        Builder (at least in a statically typed language
        programming).

        As a rule, after returning the final result to the client, an instance
        the builder must be ready to start production of the next product.
        Therefore, it is common practice to call the reset method at the end of the body
        the getProduct method. However, this behavior is optional, you
        you can make your builders wait for an explicit reset request from the code
        the client before getting rid of the previous result.
        """
        car = self._car
        self.reset()
        return car

    def produce_engine(self):
        self._car.add('Обычный двигатель')

    def produce_corpus(self):
        self._car.add('Обычный корпус')


class SuperCarBuilder(Builder):

    def __init__(self):
        """The new builder instance must contain an empty product object,
        which is used in further assembly.
        """
        self.reset()

    def reset(self):
        self._car = Car()

    def car(self):
        car = self._car
        self.reset()
        return car

    def produce_sport_engine(self):
        self._car.add('Спортивный двигатель')

    def produce_sport_corpus(self):
        self._car.add('Спортивный корпус')


class Director:
    """The Director is only responsible for performing the construction steps in a certain
    sequence. This is useful when producing products in a particular
    order or special configuration. Strictly speaking, the Director class is optional,
    since the client can directly manage the builders.
    """
    def __init__(self):
        self._builder = None

    def get_builder(self):
        return self._builder

    def set_builder(self, builder: Builder):
        """The director works with any instance of the builder that is passed to him
        client code. Thus, the client code can change the final
        the type of the newly assembled product.
        """
        self._builder = builder

    def build_sport_car(self):
        self._builder.produce_sport_engine()
        self._builder.produce_sport_corpus()

    def build_car(self):
        self._builder.produce_engine()
        self._builder.produce_corpus()


def main():
    """The client code creates a builder object, passes it to the director, and then
    initiates the build process. The final result is extracted from
    the builder object.
    """
    director = Director()
    super_car_builder = SuperCarBuilder()
    car_builder = CarBuilder()
    print('Car:')
    director.set_builder(car_builder)
    director.build_car()
    car_builder.car().list_parts()
    print('Sport car:')
    director.set_builder(super_car_builder)
    director.build_sport_car()
    super_car_builder.car().list_parts()


if __name__ == '__main__':
    main()
