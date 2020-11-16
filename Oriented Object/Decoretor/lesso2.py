def hello():
    return "Hi JOSE!"

def other(func):
    print('HELLO')
    print(func())  # i call fonction with ()

other(hello) # without () means i am not passing what hello function return