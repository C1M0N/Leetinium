"""
Course  : Leetinium
File    : AsciiArt.py
Name    : Cimon

GitHub User: C1M0N
Date: 4/16/25 01:34
"""

glyph_width_ = int(input())
glyph_height_ = int(input())
text_ = input()
glyph_ = []
for row_index in range(glyph_height_):
    glyph_.append(input())

def asciiArtGen(glyph_width, glyph_height, text, glyph):
    text_ascii = []
    for char in text:
        if ord(char.capitalize()) < 65 or ord(char.capitalize()) > 90:
            text_ascii.append(26)
        else:
            text_ascii.append(ord(char.capitalize()) - 65)

    for i in range(glyph_height):
        for char_index in text_ascii:
            print(glyph[i][char_index * glyph_width:(char_index + 1) * glyph_width], end= "")
        print()

asciiArtGen(glyph_width_, glyph_height_, text_, glyph_)

# region dev
def run_tests():
    import doctest

    doctest.testmod(verbose = True)


def main():
    run_tests()

    pass


if __name__ == "__main__":
    main()
# endregion
