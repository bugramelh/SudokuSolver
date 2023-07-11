from sudoku import Sudoku

# Sudoku(sütun,satır)
# diffuculty(x) ->  hücrelerin yüzde kaçının boş olacağını seçersin 0 ile 1 arasında değer alır.

puzzle = Sudoku(4).difficulty(0.5)
puzzle.show()

#Çözümünü ekranda çıkartmaya yarıyor.
solution = puzzle.solve()
solution.show()

