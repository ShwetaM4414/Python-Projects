from pyamaze import maze, agent, COLOR


def BFS(m):
    global Cell

    # start cell is the last cell
    start = (m.rows, m.cols)

    # creating a list
    visited = [start]
    position = [start]

    # creating a dictionary
    bfsPath = {}

    # iterate until position list becomes empty
    while len(visited) > 0:
        currentCell = position.pop(0)

        # if it meets the goal then loop will end
        # (1,1) is the goal
        if currentCell == (1, 1):
            break

        # explore each direction
        for d in 'ESNW':

            # verify if the path in that direction is open or not
            if m.maze_map[currentCell][d] == True:

                # expression for each direction
                if d == 'E':
                    Cell = (currentCell[0], currentCell[1] + 1)
                elif d == 'W':
                    Cell = (currentCell[0], currentCell[1] - 1)
                elif d == 'N':
                    Cell = (currentCell[0] - 1, currentCell[1])
                elif d == 'S':
                    Cell = (currentCell[0] + 1, currentCell[1])

                if Cell in visited:
                    # skip the remaining part and move to the next iteration
                    continue

                # appending the Cell in both list
                visited.append(Cell)
                position.append(Cell)

                # adding a key value pair in dictionary
                bfsPath[Cell] = currentCell

    # creating a dictionary
    fwdPath = {}

    # goal cell
    c = (1, 1)

    # iterate till the start cell
    while c != start:
        fwdPath[bfsPath[c]] = c
        c = bfsPath[c]
    return fwdPath


if __name__ == '__main__':
    # Creating a maze
    m = maze(20, 30)

    # Generate a random maze
    m.CreateMaze(loopPercent=40)

    # calling a function
    path = BFS(m)

    # to move agent
    a = agent(m, footprints=True, color=COLOR.red, shape='arrow')
    m.tracePath({a: path}, delay=100)

    m.run()
