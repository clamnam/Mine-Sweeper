class guess:
    def __init__(self):
        self.level = level
        self.matrix = []

        def guess(self):
            guess_x = int(input("input x coord guess : "))
            guess_y = int(input("input y coord guess : "))
            if guess_x and guess_y:
                self.matrix[guess_x][guess_y] = self.grid_array[guess_x][guess_y]

            for x, rows in enumerate(self.matrix):
                print(self.matrix[x])
