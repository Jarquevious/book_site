1. How would we filter for all books with titles containing the word ‘Django’?
    books = Books.objects.filter(title__contains='Django')

2. How would we filter for all books with tag ‘Fiction’?
    books = Books.objects.filter(tag_name ='Fiction')

3. How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!
    author_list = books.object.filter(name__contains='Django')

