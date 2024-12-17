
__author__ = "Maximilian Geitner"
__date__ = "15.12.2024"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def get_rows(level):
    return len(level)

def get_cols(level):
    return len(level[0])

def is_in_bounds(cur_x, cur_y, level):
    return 0 <= cur_x < get_cols(level) and 0 <= get_rows(level)

def get_tile(cur_x, cur_y, level):
    return level[cur_y][cur_x]

def set_tile(cur_x, cur_y, value, level):
    level[cur_y][cur_x] = value

def move_tile(cur_x, cur_y, dest_x, dest_y, level):
    tile = get_tile(cur_x, cur_y, level)
    set_tile(dest_x, dest_y, tile, level)
    set_tile(cur_x, cur_y, '.', level)

def map_letter_to_direction(letter):
    if letter == '^':
        return UP
    elif letter == '>':
        return RIGHT
    elif letter == 'v':
        return DOWN
    elif letter == '<':
        return LEFT
    else:
        print("Error Letter: ", letter)

def map_direction_to_diff(direction):
    diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    return diff[direction]

def try_to_move_in_direction(level, cur_x, cur_y, direction):
    next_x, next_y = cur_x + map_direction_to_diff(direction)[0], cur_y + map_direction_to_diff(direction)[1]
    # modification for part 2:
    # evaluate if all boxes can be moved, then act if the result is true
    if not can_move_in_direction(level, cur_x, cur_y, direction):
        return cur_x, cur_y

    if get_tile(next_x, next_y, level) == '#':
        # cannot move
        return cur_x, cur_y
    # case move left or right
    elif (get_tile(next_x, next_y, level) == '[' or get_tile(next_x, next_y, level) == ']') and (direction == LEFT or direction == RIGHT):
        # try to move next item, if it works move itself
        box_x, box_y = try_to_move_in_direction(level_map, next_x, next_y, direction)
        if next_x != box_x or next_y != box_y:
            move_tile(cur_x, cur_y, next_x, next_y, level)
            return next_x, next_y
        else:
            return cur_x, cur_y
    elif get_tile(next_x, next_y, level) == '[' and (direction == UP or direction == DOWN):
        # try to move tile one tile to the right, too
        box_x, box_y = try_to_move_in_direction(level_map, next_x, next_y, direction)
        box2_x, box2_y = try_to_move_in_direction(level_map, next_x + 1, next_y, direction)

        if (next_x != box_x or next_y != box_y) and (next_x + 1 != box2_x or next_y != box2_y):
            move_tile(cur_x, cur_y, next_x, next_y, level)
            return next_x, next_y
        else:
            return cur_x, cur_y
    elif get_tile(next_x, next_y, level) == ']' and (direction == UP or direction == DOWN):
        # try to move tile one tile to the left, too
        box_x, box_y = try_to_move_in_direction(level_map, next_x, next_y, direction)
        box2_x, box2_y = try_to_move_in_direction(level_map, next_x - 1, next_y, direction)
        if (next_x != box_x or next_y != box_y) and (next_x - 1 != box2_x or next_y != box2_y):
            move_tile(cur_x, cur_y, next_x, next_y, level)
            return next_x, next_y
        else:
            return cur_x, cur_y
    else:
        # can always move
        move_tile(cur_x, cur_y, next_x, next_y, level)
        return next_x, next_y

# check whether moving all boxes is allowed
# structure similar to method try_to_move_in_direction(), but without actual action
def can_move_in_direction(level, cur_x, cur_y, direction):
    next_x, next_y = cur_x + map_direction_to_diff(direction)[0], cur_y + map_direction_to_diff(direction)[1]
    if get_tile(next_x, next_y, level) == '#':
        # cannot move
        return False
    # case move left or right
    elif (get_tile(next_x, next_y, level) == '[' or get_tile(next_x, next_y, level) == ']') and (
            direction == LEFT or direction == RIGHT):
        # try to move next item, if it works move itself
        can_move_box = can_move_in_direction(level_map, next_x, next_y, direction)
        return can_move_box
    elif get_tile(next_x, next_y, level) == '[' and (direction == UP or direction == DOWN):
        # try to move tile one tile to the right, too
        can_move_box = can_move_in_direction(level_map, next_x, next_y, direction)
        can_move_box_2 = can_move_in_direction(level_map, next_x + 1, next_y, direction)

        return can_move_box and can_move_box_2
    elif get_tile(next_x, next_y, level) == ']' and (direction == UP or direction == DOWN):
        # try to move tile one tile to the left, too
        can_move_box = can_move_in_direction(level_map, next_x, next_y, direction)
        can_move_box_2 = can_move_in_direction(level_map, next_x - 1, next_y, direction)
        return can_move_box and can_move_box_2
    else:
        # can always move
        return True

if __name__ == '__main__':

    use_example = False
    filename = "input.txt"
    if use_example:
        filename = "example.txt"

    # 1.) Read Input
    level_map = []
    robot_input = ""
    columns_level = 0
    rows_level = 0
    robot_x, robot_y = 0, 0
    with open(filename) as file:
        phase = 0
        for line in file:
            line: str = line.replace("\n", "")
            if line == "":
                phase = 1
            elif phase == 0:
                line = line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
                level_map.append(list(line))
                if line.find('@') != -1:
                    robot_x, robot_y = line.index('@'), get_rows(level_map) - 1
            else:
                robot_input += line

    rows_level = len(level_map)
    columns_level = len(level_map[0])
    # 2.) simulate robot movement
    for movement in robot_input:
        direction_robot = map_letter_to_direction(movement)
        robot_x, robot_y = try_to_move_in_direction(level_map, robot_x, robot_y, direction_robot)

    solution = 0
    # 3.) calculate gps coordinates
    for j in range(rows_level):
        print(''.join(level_map[j]))    # show map
        for i in range(columns_level):
            tile_value = get_tile(i, j, level_map)
            if tile_value == '[':
                # calculate dist to edge
                solution += (100 * j + i)
    # 4.) output result
    print("Solution Day 15 Part 2: ", solution)
