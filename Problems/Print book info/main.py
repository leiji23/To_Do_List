def print_book_info(title, author=None, year=None):
    title_part = f'"{title}"'
    was_written = ' was written'
    author_part = f' by {author}'
    year_part = f' in {year}'
    if author is None and year is None:
        print(title_part)
    elif author is None:
        print(title_part + was_written + year_part)
    elif year is None:
        print(title_part + was_written + author_part)
    else:
        print(title_part + was_written + author_part + year_part)
