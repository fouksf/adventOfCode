input = open("2021/4/input.txt", "r").read().split("\n\n")


class Field:
    def __init__(self, number, is_marked):
        self.number = number
        self.is_marked = is_marked
    
    def mark(self):
        self.is_marked = True

class BingoBoard:
    def __init__(self, numbers):
        self.numbers = [number for row in numbers for number in row]
        self.board = list(map(lambda row: list(map(lambda n: Field(n, False), row)), numbers))
        self.ignore = False
    
    def mark_number(self, number):
        if number in self.numbers:
            index = self.numbers.index(number)
            row =  index // 5
            column = index % 5
            self.board[row][column].is_marked = True
    
    def has_won(self):
        for row in self.board:
            if all(map(lambda field: field.is_marked, row)): 
                return True
        for i in range(0, 5):
            if all(map(lambda row: row[i].is_marked, self.board)):
                return True
        return False

    def sum_of_unmarked(self):
        return sum(list(map(lambda row: sum(map(lambda field: 0 if field.is_marked else int(field.number), row)), self.board)))

    def should_ignore(self):
        return self.ignore
        

winning_numbers = input[0].split(',')
boards = list(map(lambda b: BingoBoard(list(map(lambda c: c.split(), b.split('\n')))), input[1:]))

boards_won = 0
all_boards = len(boards)
for number in winning_numbers:
    for board in boards:
        if board.should_ignore():
            continue
        board.mark_number(number)
        if(board.has_won()):
            board.ignore = True
            boards_won += 1
            if all_boards - boards_won == 0:
                print(board.sum_of_unmarked() * int(number))