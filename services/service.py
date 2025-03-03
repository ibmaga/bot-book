import sys
import os


BOOK_PATH = 'books/book.txt'
PAGE_SIZE = 1200
book: dict[int, str] = {}


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end = start + page_size if start + page_size < len(text) else len(text)
    words: str = text[start: end].lstrip('.,!<>:')
    chars = '.!:;?'

    sentence = words.replace('\n', ' ')
    while (end != len(text) and text[end] in chars and sentence[-1] in chars) or sentence[-1] not in chars:
        sentence = sentence[:-1]
        end -= 1
    return sentence.lstrip(), len(sentence)


def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as f:
        text = f.read()
    cnt, i = 0, 1
    while cnt != len(text):
        page, length = _get_part_text(text, cnt, PAGE_SIZE)
        book[i] = page.lstrip()
        i += 1
        cnt += length

prepare_book(os.path.join(sys.path[1], os.path.normpath(BOOK_PATH)))
