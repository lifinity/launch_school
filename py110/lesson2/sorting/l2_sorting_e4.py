# how would you sort following list of dicts based on yr of
# publication of each book, from earliest to most recent

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def book_year_published(dict):
    return int(dict['published'])

# problem didn't specify mutation or not, but if non-mutating
# sorted_books = sorted(books, key=book_year_published)
books.sort(key=book_year_published)
print(books == 
    [
        {
            'title': 'The Book of Kells',
            'author': 'Multiple Authors',
            'published': '800'
        },
        {
            'title': 'War and Peace',
            'author': 'Leo Tolstoy',
            'published': '1869'
        },
        {
            'title': 'One Hundred Years of Solitude',
            'author': 'Gabriel Garcia Marquez',
            'published': '1967'
        }
    ])