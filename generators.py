# def numbers():
#     print("Starting")
#     yield 10

#     print("Middle")
#     yield 20

#     print("Ending")
#     yield 30
# n=numbers()
# print(next(n))
# print(next(n))
# # for n in numbers():
# #     print("Value:", n)


# numbers=(x*x for x in range(5))


# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(list(numbers))



# def sample():
#   yield
# s=sample()
# print(next(s))
# s.send(100)
# print(next(s))
# def test():
#     x = yield 1
#     print("Received:", x)
#     yield 2
#     yield 4


# g = test()

# print(next(g))
# print(g.send(3))



class MyNumbers:

    def __init__(self):
        self.n = 1

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self.n <= 3:
            value = self.n
            self.n += 1
            return value

        raise StopIteration 


n=MyNumbers()

print(next(n))
print(next(n))
# for i in n:
#     print(i)