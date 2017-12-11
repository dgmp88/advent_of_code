import data

def jump(position, message):
    val = message[position]
    message[position] += 1
    return val

def jump_2(position, message):
    val = message[position]
    if val >= 3:
        message[position] -= 1
    else:
        message[position] += 1
    return val


def exit(message, fn=jump):
    message = message.copy()
    steps = 0
    position = 0

    while True:
        jump_amount = fn(position, message)
        position += jump_amount
        steps += 1
        if position >= len(message) or position < 0:
            break
    return steps

assert exit(data.test_data) == 5
print('Part 1 result = {}'.format(exit(data.data)))

assert exit(data.test_data, fn=jump_2) == 10
print('Part 2 result = {}'.format(exit(data.data, fn=jump_2)))
