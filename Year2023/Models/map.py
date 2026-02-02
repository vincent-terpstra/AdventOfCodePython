class Map:
    def __init__(self, lines):
        self.lines = lines
        self.height = len(lines)
        self.width = len(lines[0])

    def __str__(self):
        return f'{self.height} : {self.width}'

    def get_rows(self):
        return map(Row, zip(range(0, self.height), self.lines))

    def get(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return '.'
        else:
            return self.lines[y][x]


class Row:
    def __init__(self, line):
        self.y = line[0]
        self.line = line[1]
        self.width = len(self.line)

    def get_numbers(self):
        return iter(self)

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        total = 0
        x = 1000
        while self.x < self.width:
            at = self.line[self.x]
            if at.isdigit():
                x = min(x, self.x)
                total = total * 10 + int(at)
            elif total != 0:
                return x,  total
            self.x += 1

        if total != 0:
            return x, total
        raise StopIteration
