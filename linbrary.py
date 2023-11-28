class Book:
    def __init__(self ,  title , author , ISBN , pages , price):
        self.title =  title
        self.author =  author
        self.ISBN =  ISBN
        self.pages =  pages
        self.price = price

    def display_book(self):
        print(f" Title : { self.title}")
        print(f" author : { self.author}")
        print(f" ISBN : { self.ISBN}")
        print(f" pages : { self.pages}")
        print(f" price : { self.price}")


class RefernceBook(Book):
    def __init__(self , reference_matrial , title , author , ISBN , pages , price ):
        super().__init__ (title , author , ISBN , pages , price)
        self.reference_matrial = reference_matrial

    def display_deails(self ):
        super().display_book()
        print(f" Referance : {self.reference_matrial}")


class FictionBook(Book):
    def __init__(self , genre ,  title , author , ISBN , pages , price):
        super().__init__(title , author , ISBN , pages , price)
        self.genre = genre

    def display_deails(self):
        super().display_book()
        print(f" Genre : {self.genre}" )      


class Liberary:

    # fiction_book = FictionBook()

    new_dict = {}

    def add_book(self,book):
        self.new_dict[book.title] = book
        
    def display_dict(self):
        for book in self.new_dict.values():
            book.display_book()
    
    def search_book(self , title):
        if title in self.new_dict:
            book = self.new_dict[title]
            print(f" Searched Book  : {book.title}")
            print (f" Author : {book.author}")
            print (f" ISBN : {book.ISBN}")
            print (f" Pages : {book.pages}")
            print (f" Price : {book.price}")
        else:
            print( " book not found ")
    # def search_book(self , title):
    #     val = 1
    #     for title in self.new_dict:
    #         if self.new_dict[title] == val:
    #             res = title
    #     print(f" Title of book is : " + str(res) )

    def remove ( self , title ):
        # for title in self.new_dict:
        if title in self.new_dict:
            book = self.new_dict[title]
            del self.new_dict[title]
            print (f" book is removed : {book.title}")
            print (f" Author : {book.author}")
            print (f" ISBN : {book.ISBN}")
            print (f" Pages : {book.pages}")
            print (f" Price : {book.price}")
        else:
            print(" title not found")

     
def main():

    liberary = Liberary()

    # reference_book = RefernceBook() This instance o calss you can give attributes to it.
    reference_book = RefernceBook("atlas" , "THE ORIGINALS THE RISE (The Originals, 1)" ,
                                "Smithsonian Institution" , 1234567 , 500 ,
                                "44.99 dollar \n")
    # reference_book.display_deails()
    liberary.add_book(reference_book)
        
    fiction_book = FictionBook("science_fiction" , "History of the World Map by Map" ,
                                "Julie Plec" , 
                                9876543 , 351 ,
                                "12.99 dollar")
    # fiction_book.display_deails()

    liberary.add_book(fiction_book)
    liberary.display_dict()
    liberary.remove("THE ORIGINALS THE RISE (The Originals, 1)")
    liberary.search_book("History of the World Map by Map" )
    # liberary.search_book("THE ORIGINALS THE RISE (The Originals, 1)")


    
main()








    # reference_book.atlas = { " Title " : " History of the World Map by Map " ,
    #           " Author " : "Smithsonian Institution" ,
    #           " ISBN " : 1234567 ,
    #           " Pages " : 500 ,
    #           " Price " : "44.99 dollar"
    #          }
    # fiction_book.science_fiction = { " Title " : " THE ORIGINALS THE RISE (The Originals, 1) " , 
    #                     " Author " : " Julie Plec " , 
    #                     " ISBN " : 9876543 , 
    #                     " Pages " : 351 , 
    #                     " Price " : " 12.99 dollar"
    #                   }
    # liberary = Liberary()
        # self.add_book[book.title]=book
        # if book is reference_book:
        #     Liberary.add_book(reference_book)
        #     print (f" Reference material is added : {reference_book}")
        # else:
        #     Liberary.add_book(fiction_book)
        #     print (f" Fiction Book is added : {fiction_book}")















    # def add_book( self , book  ):
    #     a = input ( " Enter Key you want to add" )
    #     b = input ( " Enter value you want to add" )
    #     self.new_dict [a] += [b]
    #     print ( " new added values are : " )

    # def all_book_details( self , book ):
    #     for book in self.new_dict:
    #         if self.new_dict:
    #             print( " Here ara all the books : " )
    #         else:
    #             print( " Liberary is empty : " )

    # def search_book_by_title( self , book , title ):
    #     for book in self.new_dict:
    #         if book.title.lower() == title.lower():
    #             if self.new_dict:
    #                 print ( " Book according to your search is : " )
    #             else :
    #                 print ( " No book found : " )

    # def remove_book( self , book , title ):
    #     for book in self.new_dict:
    #         if book.title.lower() == title.lower():
    #             if self.new_dict:
    #                 a = input (" Enter key you want to remove")
    #                 self.new_dict.pop(a)
    #                 print ( " Book is removed : " )
    #             else: 
    #                 print( " No book exist : " )

