class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


def main():
    a = Singleton()
    b = Singleton()
    print(a is b)


if __name__ == '__main__':
    main()
