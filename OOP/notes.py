# class Book():
    
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

#     def __len__(self):
#         return self.pages
    
#     def __del__(self):
#         print("a book is destroyed.")


# myBook = Book("Python", "Jose", 200)
# del myBook

class Animal():
    
    def __init__(self):
        print("Animal")

    def eat(self):
        print("Animal eating")

class Dog(Animal):
    def __init__(self):
        pass

    def bark(self):
        print("I am Barking")


myDog = Dog()
myDog.eat()