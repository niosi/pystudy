def MyGenerator():
    value = (yield 1)
    value2 = (yield value)
    value3 = (yield value2)


gen = MyGenerator()
print(gen.send(None))
print(gen.send(2))
print(gen.send(3))
