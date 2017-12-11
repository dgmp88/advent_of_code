
def calc_distance(num)
    # This calculates the result without needing to run the whole grid, which I wanted to avoid as that would
    # get expensive for large grids. It was silly though as part 2 of the test required the whole grid anyway
    #
    # Grid edge length goes 3, 5, 7
    # Total edges goes 8, 16, 24, 32
    # First outer = 2, 10, 26, 50
    # First, calculate the box distance it belongs to
    if num == 1
        return 0
    end
    num = Float(num)
    start = 1
    fin = 1
    x = 0
    edge_length = 0
    loop do
        if num >= start and num <= fin
            break
        end
        start = (fin + 1)
        x += 1
        edge_length = 1 + (2 * x)
        total_edges = (4 * edge_length) - 4
        fin = start + total_edges - 1
    end


    # start y = 0, 1, 2, 3
    y = x
    y_n = start
    change = -1
    loop do
        y += change

        if y_n == num
            break
        end

        if y == 0 or y == x
            change = -change
        end

        y_n += 1
    end


    dist = x + y
    return dist
end


def test()
    tests = [[1,0], [2, 1], [3, 2], [4, 1], [9, 2], [12,3], [23, 2], [1024, 31]]
    for test in tests
        res = calc_distance(test[0])
        raise "Failed #{test[1]} != #{res}, for #{test[0]}" unless res == test[1]
    end
end

class Grid
    # This class manages computing the entire grid for part 2 of the challenge
    
    attr_reader :num
    def initialize()
        @grid = [[1]]
        @size = 1

        # x/y = current position
        @x = 0
        @y = 0

        @adjacent = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
        @num = 1
    end

    def expand()
        @size += 2
        for line in @grid
            line.push(0)
            line.unshift(0)
        end
        @grid.unshift(Array.new(@size, 0))
        @grid.push(Array.new(@size, 0))
        @x += 1
        @y += 1
    end

    def print()
        for line in @grid
            puts("#{line}")
        end
    end

    def fill()
        # Get the sum of all adjacent squares
        move
        sum = @grid[@y][@x]

        for coords in @adjacent
            x = @x + coords[0]
            y = @y + coords[1]
            if x >= 0 and x <= (@size - 1) and y >= 0 and y <= (@size-1)
                val = @grid[y][x]
                sum += val
            end
        end

        @grid[@y][@x] = sum
    end

    def current()
        return @grid[@y][@x]
    end

    def move()
        # If it's the first move after an expand, move right
        size = @size - 1

        if @y == size and @x == size
            expand
            @x += 1
        # If we're on the right edge, move up or left one
        elsif @x == size and @y > 0
            @y -= 1
        elsif @x == size and @y == 0
            @x -= 1
        # If we're at teh top, move left or down one
        elsif @y == 0 and @x > 0
            @x -= 1
        elsif @y == 0 and @x == 0
            @y += 1
        # Left edge, down or right
        elsif @x == 0 and @y < size
            @y += 1
        elsif @x == 0 and @y == size
            @x += 1
        elsif @y == size and @x < size
            @x += 1
        end
        @num += 1
    end
end

def test_two(grid)
    tests = [[1, 1], [2, 1], [3, 2], [4, 4], [5, 5]]

    for test in tests
        num = test[0]
        res = test[1]
        while grid.num() < num do
            grid.fill
        end 
        raise "Failed #{grid.current} != #{res}, for #{num}" unless grid.current == res
    end
end

def one(test_val)
    test()
    res1 = calc_distance(test_val)
    puts("Result is #{res1}")
end

def two(test_val)
    grid = Grid.new()
    test_two(grid)
    while grid.current <= test_val do
        grid.fill
    end 
    puts("Result is #{grid.current}")
end

test_val = 277678
one(test_val)
two(test_val)
