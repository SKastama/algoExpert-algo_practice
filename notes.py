# OOP basics
class Book():
    
    favorites = []

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False
    
    # String format of output
    def __str__(self):
        return "{} is {} long".format(self.title, self.pages)

    # String comparisisms
    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        return False
    
    # Most functions need something hashable. Classes and lists are not hashable
    # Use hash when using mutable data
    # __hash__ = None # mutable
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)

book1 = Book("Title1", 72)
book2 = Book("Title2", 172)

Book.favorites.append(book1)
Book.favorites.append(book2)

# Prints favorite books
# for b in Book.favorites:
#     print(b)

book3 = Book("Title34", 72)
book4 = Book("Title34", 72)

# Sees if books are the same book
# print(book3 == book4)

# hashes shouldnt change, two itdentical objects hashes should be the same, 
# different objects can have the same hashes and its fine
print(hash(book3) == hash(book4))