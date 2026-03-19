# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation.
# class Robot:
#     def move(self) -> bool:
#     def turnLeft(self) -> None:
#     def turnRight(self) -> None:
#     def clean(self) -> None:
# """

class Solution:
    def cleanRoom(self, robot):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(row, col, d):
            visited.add((row, col))
            robot.clean()

            for i in range(4):
                new_d = (d + i) % 4
                dr, dc = directions[new_d]
                new_row, new_col = row + dr, col + dc

                if (new_row, new_col) not in visited and robot.move():
                    backtrack(new_row, new_col, new_d)
                    go_back()

                robot.turnRight()

        backtrack(0, 0, 0)