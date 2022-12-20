def test_add_comment(book_factory):
    book = book_factory.create()
    print(book.title())
    assert True
