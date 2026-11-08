from collections import deque
import random

class Square:
    def __init__(self, status: str):
        """
        each of the squares on the grid is an object from this class
        :param status: each square has an attribute that determines the status of the square
        which could either be free, brick, treasure, pit
        """
        self.status = status

class Grid:
    def __init__(self, level, method):
        """
        the grid or environment of the agent is an object from this class
        :param level: the level could be easy, medium or hard which effects the number of bricks, pits and treasures
        :param method: I have done task 14 and 15 and this parameter determines which task should be run
        random for 14 and backtracking for 15
        """
        self.level = level
        self.method = method

        if level == "easy":
            self.brick_num = 5
            self.pit_num = 0
            self.treasure_num = 2

        elif self.level == "medium":
            self.brick_num = 8
            self.pit_num = 2
            self.treasure_num = 3


        elif self.level == "hard":
            self.brick_num = 12
            self.pit_num = 4
            self.treasure_num = 5

        # at first all squares are free in the grid
        self.grid = []
        for i in range(0, 64):
            self.grid.append(Square("free"))

        self.set_up_grid()
        self.visualize()

    def set_up_grid(self):
        """
        it is assumed that the pits and breaks placement is done by someone else. since I wanted to test this part of
        the code, I set the brick's placement and pit's placement at random
        whether the random method or the backtracking method is used the suitable treasure placement function is
        called
        :return: nothing
        """
        available = [i for i in range(1, len(self.grid))] #index

        # put bricks
        for i in range(self.brick_num):
            idx = random.choice(available)
            self.grid[idx].status = "brick"
            available.remove(idx)

        # put pits
        for i in range(self.pit_num):
            idx = random.choice(available)
            self.grid[idx].status = "pit"
            available.remove(idx)

        if self.method == "random":
            for i in range(self.treasure_num):
                idx = random.choice(available)
                self.grid[idx].status = "treasure"
                available.remove(idx)


        elif self.method == "backtracking":
            self.place_treasures_backtrack()


    def place_treasures_backtrack(self):
        """
        this function collects all the free squares (except for the first one) and the shuffles them so that this
        treasures wouldn't be set right next to each other and then sends the domain to the backtracking function to
        find an answer
        :return: whether it found the answer or not
        """
        # find the domain
        treasure_domain = []
        for i in range(1, len(self.grid)):
            if self.grid[i].status == "free":
                treasure_domain.append(i)

        # shuffle the domain
        randomized_domain = []
        n = len(treasure_domain)
        for i in range(0, n):
            idx = random.choice(treasure_domain)
            randomized_domain.append(idx)
            treasure_domain.remove(idx)

        success = self.backtrack(randomized_domain, [])

        return success

    def backtrack(self, treasure_domain, assignment):
        """
        this function is a recursive function that checks for the spots that can hold the treasure and be reachable at
        the same time
        :param treasure_domain:the free squares and the non-rejected squares
        :param assignment: the set of squares that can be treasure holders
        :return: a boolean. if there is a solution it returns True. otherwise it returns false
        """
        # all treasures placed
        if len(assignment) == self.treasure_num:

            for i in assignment:
                self.grid[i].status = "treasure"
            return True

        for cell in treasure_domain:

            # two treasures won't be in one place
            if cell in assignment:
                continue

            # treasures being reachable
            if not self.is_reachable(cell):
                continue

            assignment.append(cell)

            result = self.backtrack(treasure_domain, assignment)

            if result:
                return True

            # meaning this sequence of treasures are not suitable
            assignment.pop()

        return False

    def is_reachable(self, target):
        """
        here we try to find a way to a treasure while navigating through the pits and the breaks
        :param target: the square containing the treasure
        :return: a boolean. if the treasure is reachable the boolean is true and otherwise it is false.
        """
        start = 0

        visited = set()
        queue = deque([start])

        while queue:

            current = queue.popleft()

            if current == target:
                return True

            if current in visited:
                continue

            visited.add(current)

            row = current // 8
            col = current % 8

            neighbors = []

            if row > 0:
                neighbors.append(current - 8)

            if row < 7:
                neighbors.append(current + 8)

            if col > 0:
                neighbors.append(current - 1)

            if col < 7:
                neighbors.append(current + 1)

            for n in neighbors:

                if n in visited:
                    continue

                if self.grid[n].status in ("brick", "pit"):
                    continue

                queue.append(n)

        return False

    def visualize(self):
        """
        when this function is called, the treasures are placed and the job is done. this function visualises the
        environment showing an empty space if the square is free, a P if the square contains a pit and  a B if the
        square is occupied by a brick
        :return: nothing
        """
        counter = 0
        for i in self.grid:
            counter += 1
            if i.status == "free":
                print(" ", end=" | ")
            elif i.status == "pit":
                print("P", end=" | ")
            elif i.status =="brick":
                print("B", end=" | ")
            elif i.status =="treasure":
                print("T", end=" | ")
            if counter % 8 == 0:
                print("\n", end="")
