# Hello Class
from multiprocessing.context import SpawnContext


class Hello:
    # Say Hello Function to greet the user.
    def sayHello(self, name, space):
        if (space == True and name == ""):
            return "Hello, good-for-nothing-brat!"
        elif (space == False): return "Hello!"
        return f"Hello, {name}!"
    def sayHelloP(self, name, space):
        print(self.sayHello(name, space))
