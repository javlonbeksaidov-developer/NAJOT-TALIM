from app import Book


def main():
    book = Book('', '', 0)
    while True:
        menu = '''
====== Library menegment ======

1. add
2. delete
3. update
4. show
0. exit
'''
        print(menu)
        tanlov = input(">>> ")
        if tanlov == '0':
            break
        elif tanlov == '1':
            print(book.add())
        elif tanlov == '2':
            book.delete()
        elif tanlov == '3':
            book.update()
        elif tanlov == '4':
            book.show()
        else:
            print("XATO")


if __name__ == '__main__':
    main()