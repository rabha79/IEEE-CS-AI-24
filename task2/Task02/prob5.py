# Create a dictionary representing a library catalogue.
# Each book should have a title, author, and publication year.

library = {"book1": ["horror", "rabha", 1990], "book2": ["imagnation", "lalala", 1200],
           "book3": ["drama", "queen", "2000"]}
print(library.get("book2"))
library.update({"book4": ["fantesy", "blabla", 1890]})
library.pop("book1")
print(library)
keys = library.keys()
print(keys)
values = library.values()
print(values)
