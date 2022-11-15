# TODO: add arguments
from operator import indexOf


ALLOW = 'abcdef0123456789'

# TODO: Add another SHA algorithm
SHA_1 = 40
SHA = SHA_1

SALT = 3


def is_sha(txt):
    if len(txt) == SHA:
        for i in txt:
            if not i in ALLOW:
                return False
        return True
    return False


def decrypt_sha(hsh, mult=1):
    res = ''
    for i, j in hrange(hsh, mult=mult):
        idx = indexOf(ALLOW, i) - j
        while idx < 0:
            idx += len(ALLOW)
        res += str(idx)
    return res


def hrange(txt, start=0, mult=1):
    return zip(txt, range(start, SHA*SALT*mult, SALT))


def nchr(txt):
    return str(ord(txt))


def get_symb(idx):
    return ALLOW[idx % len(ALLOW)]


def main(txt):
    if is_sha(txt):
        print("\nDecrypted ->", f'\n{decrypt_sha(txt)}')
    else:
        print("\nEncrypting...")
        txt += '%'*(SHA - len(txt))
        print(txt)

        hsh = ''
        lastk = 0
        print("\nHash ->")
        for i in txt:
            for j, k in hrange(nchr(i), lastk, SALT):
                hsh += get_symb(int(j) + k)
                lastk = k + SALT
        print(hsh)

        print("\nHash Decrypted ->")
        dec_hash = decrypt_sha(hsh, SALT)
        print(dec_hash)

        key = ''
        print("\nKey ->")
        for i, j in hrange(txt):
            key += get_symb(len(nchr(i)) + j)
        print(key)

        print("\nKey Decrypted ->")
        dec_key = decrypt_sha(key)
        print(dec_key, "\n")

        i = 0
        for val in dec_key:
            len_idx = i+int(val)
            print(chr(int(dec_hash[i:len_idx])), end='')
            i = len_idx
        print('\n\nSuccess!\n')


# TODO: Encrypt and decrypt rot47
def rot47():
    pass


# TODO: Encrypt and decrypt rot13
def rot13():
    pass


# TODO: Add cool animations
if __name__ == '__main__':
    main("tbw' (yd+ {{&\" q)'+ zp#x tar\" yr)& #auh")
    main("40c917ee4b51c646e2db376a7cc8743a19ca9ed4")
    main("Hola me llamo Ricardo!")
