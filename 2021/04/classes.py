class Cell():
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark(self):
        self.marked = True

class Line(list):
    def __init__(self, cells):
        self.cells = cells

    def complete(self):
        for cell in self.cells:
            if not cell.marked:
                return False
        return True

class Board(list):
    def __init__(self, lines):
        self.lines = lines
        self.done = False

    def complete(self):
        for line in self.lines:
            if line.complete():
                return True
        return False
    
    def unmarked_sum(self):
        total = 0
        for line in self.lines:
            for cell in line.cells:
                if not cell.marked:
                    total += cell.number
        return total // 2

    def update(self, number):
        for line in self.lines:
            for cell in line.cells:
                if cell.number == number:
                    cell.mark()