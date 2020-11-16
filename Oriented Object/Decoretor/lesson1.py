

# s = 'GLOBAL VARIABLE'
#
# def func():
#     global s
#     s=50
#     print(s)
#
# func()
# print(s)

def func(name='kimbo'):
    print(name)
    # print(locals())
    # print(globals())
    def greet():
        return "Second fonction"
    if name == "kimbo":
        return greet

x= func()

print(x())

