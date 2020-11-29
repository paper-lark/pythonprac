from typing import List, Optional, Tuple, Generator, Callable


def ls_transcodings(encodings: List[str]) -> Generator[Tuple[str, str], None, None]:
    for e in encodings:
        for d in encodings:
            if e != d:
                yield d, e


def find_encodings(reference: bytes, encodings: List[str], is_ok: Callable[[bytes], bool]) -> Generator[List[Tuple[str, str]], None, None]:
    def inner(text: bytes, stack: List[Tuple[str, str]]) -> Generator[List[Tuple[str, str]], None, None]:
        if len(stack) >= 4:
            return None

        for d, e in ls_transcodings(encodings=encodings):
            if len(stack) > 0 and d == stack[-1][1]:
                continue
            try:
                translated = text.decode(d).encode(e)
                stack.append((d, e))
                if is_ok(translated):
                    yield stack
                for match in inner(translated, stack):
                    yield match
                stack.pop()
            except UnicodeDecodeError:
                pass
            except UnicodeEncodeError:
                pass

    for result in inner(reference, []):
        yield result


def main():
    encodings = input().strip().split(' ')
    text = bytes.fromhex(input())

    def is_ok(t: bytes):
        return text.startswith(t)

    reference = 'ПРОЦ'.encode('koi8-r')
    for match in find_encodings(reference, encodings, is_ok=is_ok):
        try:
            decoded = text
            for d, e in reversed(match):
                decoded = decoded.decode(e).encode(d)
            result = decoded.decode('koi8-r')
            print(result)
            break
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass


if __name__ == '__main__':
    main()
