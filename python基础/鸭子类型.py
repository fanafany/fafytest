class Duck:
    def quack(self):
        print("guagua")


class Person:
    def quack(self):
        print("我是人类")

def in_the_forest(duck):
    duck.quack()


def game():
    don = Duck()
    john = Person()
    in_the_forest(don)
    in_the_forest(john)


game()