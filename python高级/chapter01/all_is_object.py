def ask(name = "fanafany"):
    print(name)
# my_name = ask
# my_name("haha")

class Person:
    def __init__(self):
        print("fafy")
# my_class = Person
# my_class()

object_list = []
object_list.append(ask)
object_list.append(Person)
for item in object_list:
    print(item())

def decorator_func():
    print("dec start")
    return ask

# my_ask = decorator_func()
# my_ask('demo')

