from functools import wraps

def outer(func):

    @wraps(func)
    def wrapper():
        print("function")

    return wrapper


@outer
def hello():
    print("hello")

print(hello.__name__)


def test():
    return 10
