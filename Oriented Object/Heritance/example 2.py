class Book():
    def __init__(self, title, author, pages):

        self.title=title
        self.author= author
        self.pages = pages

    def __str__(self):  # special methode for string representation
        return "Title: {}, Author: {}, Pages:{}".format(self.title, self.author, self.pages)

    def __len__(self):  # special methode for string len
        return self.pages  # on specifie ce qu on veut voir

    def __del__(self):
        print(" a book is destroyed ")

b = Book('Python', 'Kimbo', 300)
print(b)

print(len(b))

del b
print(b)