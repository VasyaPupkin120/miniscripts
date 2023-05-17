# Вывод красивого текста в консоль
# Библиотека устанавливается стандартно - pip install pyfiglet
# Список всех шрифтов: f = pyfiglet.Figlet(); f.getFont()

import pyfiglet

TEXT_SAMPLE = "Sample font"
GOOD_FONTS = [
        "mirror",
        "banner",
        "char3___",
        "ogre",
        "starwars",
        "linux",
        "big",
        "rounded",
        "moscow",
        "stop",
        "doom",
        "cosmike",
        "slant",
        "isometric1",
        "small",
        "doh",
        "roman",
        "speed",
        "epic",
        "standard",
        "puffy",
        "utopia",
        "tombstone",
        "serifcap",
        "shimrod",
        ]


def printAscii(text="Hello", font="epic", justify="center", width=120):
    """
    Вывод текста с некоторыми предустановками.
    """
    print(pyfiglet.figlet_format(text, font=font, justify=justify, width=width))


def printSampleGood(text=TEXT_SAMPLE):
    """
    Вывод образцов понравившихся шрифтов.
    """
    for font in GOOD_FONTS:
        print(f"Font: {font}\n\n")
        printAscii(text, font=font)
        print("\n\n")


def printSampleAll(text=TEXT_SAMPLE):
    """
    Вывод образцов всех шрифтов.
    """
    pyfiglet_object = pyfiglet.Figlet()
    for font in pyfiglet_object.getFonts():
        print(f"Font: {font}\n\n")
        printAscii(text, font=font)
        print("\n\n")


def printStart():
    """
    Красивые строчки приветствия
    """
    TEXT_START = "-"*10 + "\nStart\npyfiglet\n" + "-"*10
    printAscii(text=TEXT_START, font="epic")

        
if __name__ == "__main__":
    printStart()
    # printSampleGood()
