import os
import sys


def _get_part_text(text, start, page_size):
    result = text[start:start + page_size]
    punctuation_marks = ',.!:;?'
    if start + page_size >= len(text)-1 or (result[-1] in punctuation_marks and text[start + page_size] not in punctuation_marks):
        return result, len(result)
    for i in range(len(result)-2, 0, -1):
        if result[i] in punctuation_marks and result[i+1] not in punctuation_marks:
            return result[:i+1], len(result[:i+1])
    return result, len(result)


path = 'book/book.txt'
book: dict[int, str] = {}
PAGE_SIZE = 1050
with open(path, encoding='utf-8') as file:
    file = file.read()


def prepare_book(path: str) -> None:
    count = 1
    i = 0
    while i < len(file):
        result = _get_part_text(file, i, PAGE_SIZE)
        book[count] = result[0].lstrip()
        i += result[1]
        count += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(path)))
