''' 
Topic: class and object
    class: A blueprint for which object is create.
    object: an instant of a class

example :
     class = main book
     objects = copy of main book(update of the main book)

'''
class Main_book:
    book_name = "Python Book"
    author = "KzRaihan"
    age = 23
    book_page = 250
    
    def display_info(self):
        print("Book name: ",self.book_name)
        print("Author: ", self.author)
        print("Age  : ", self.age)
        print("Book page: ", self.book_page)
        
    
first_audition = Main_book()
first_audition.display_info()
