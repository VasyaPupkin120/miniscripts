"""
Заполнение окна символами без особого смысла - просто прикольно.
"""
import time
import random

HEIGHT = 40
WIDTH = 100
LIST_SYM = ["X", "O", "I", "G", " "]

MAIN_LINE = " " * WIDTH
MAIN_MATRIX = []
for i in range(HEIGHT):
    MAIN_MATRIX.append(MAIN_LINE)


def clearWin():
    """
    Очищает окно без изменения матрицы.
    """
    clearLine = " " * WIDTH + "\n"
    clearMatrix = clearLine * HEIGHT
    print(clearMatrix)


def printWin():
    """
    Распечатывает все окно.
    """
    print("\n".join(MAIN_MATRIX), flush=True)


def replaceOneSym(numRow: int, numCol: int, sym: str):
    """
    Получает один символ и координаты (номер строки и номер столбца)
    Устанавливает этот символ в глобальном списке.
    """
    changeRow = MAIN_MATRIX[numRow]
    newRow = changeRow[:numCol] + sym +changeRow[numCol+1:]
    MAIN_MATRIX[numRow] = newRow


def printHLine(row: int, startCol: int, stopCol: int, sym: str = "-"):
    """
    Выводит одну горизонтальную линию.
    Включаются оба конца, сделать линию из одного символа не получится.
    """
    if startCol > stopCol:
        startCol, stopCol = stopCol, startCol
    if startCol == stopCol:
        exit()

    changeRow = MAIN_MATRIX[row]
    lenHLine = stopCol - startCol
    newRow = changeRow[:startCol] + sym*lenHLine +changeRow[stopCol+1:]
    MAIN_MATRIX[row] = newRow


def printVLine(col: int, startRow: int, stopRow: int, sym: str = "-"):
    """
    Выводит одну вертикальную линию.
    Включаются оба конца, сделать линию из одного символа не получится.
    """
    if startRow > stopRow:
        startRow, stopRow = stopRow, startRow
    if startRow == stopRow:
        exit()

    for row in range(startRow, stopRow + 1):
        changeRow = MAIN_MATRIX[row]
        newRow = changeRow[:col] + sym +changeRow[col+1:]
        MAIN_MATRIX[row] = newRow

    
    


def mainLoop():
    """
    Основной цикл вывода.
    """
    while True:
        clearWin()

        # ввод блинкующего символа
        randRow = random.randrange(HEIGHT)
        randCol = random.randrange(WIDTH)
        randSym = random.choice(LIST_SYM)
        replaceOneSym(randRow, randCol, randSym)

        # ввод рамки окна
        printHLine(row=0, startCol=0, stopCol=WIDTH-1, sym="=") 
        printHLine(row=HEIGHT-1, startCol=0, stopCol=WIDTH-1, sym="=") 
        printVLine(col=0, startRow=0, stopRow=HEIGHT-1, sym="I")
        printVLine(col=WIDTH-1, startRow=0, stopRow=HEIGHT-1, sym="I")

        # распечатка символа и рамки.
        printWin()
        time.sleep(0.01)

        # блинкующий символ пустой
        # replaceOneSym(randRow, randCol, " ")





def main():
    mainLoop()

if __name__ == "__main__":
    main()
