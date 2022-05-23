"""
This program keeps track of all of our books
version : 2.0.0
Date :15.05.2022
"""


def main():
    
    try:    
        # initialize books list
        booksList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(",") )
            line = infile.readline()
        infile.close()
        
    except FileNotFoundError :
        print("the <bookslist.txt> file is not found ")
        print("Starting a new books list!")
        booksList = []    
    
    choice = 0
    while choice !=4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())
        
        if choice == 1:
            print("Addig a book...")
            nBook = input("Enter the name of the book >>>")
            nAuthor = input("Enter the name of the author >>>")
            rBefore = input("Have you read it before ? >>>")
            nPages = input("Enter the number of pages >>>")
            booksList.append([nBook, nAuthor, rBefore, nPages])
        
        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter Search Term: ")
            for book in booksList:
                if keyword in book:
                    print(book)
        
        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])
        
        elif choice == 4:
            print("Quitting Program")
    print("Program Terminated!")
    
    # Saving to external TXT file
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()
                    


if __name__ == "__main__":
    main()