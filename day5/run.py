import os

def parse_line(line) -> dict: 
    rows_start = 0
    rows_end = 127
    cols_start = 0
    cols_end = 7
    row_check = line[0:7]
    col_check = line[7:]

    for l in row_check:
        if l == 'F':
            rows_end = rows_start + int(abs(rows_start-rows_end+1)/2)
        elif l == 'B':
            rows_start = rows_end - int(abs(rows_start-rows_end+1)/2)

    for l in col_check:
        if l == 'L':
            cols_end = cols_start + int(abs(cols_start-cols_end+1)/2)
        elif l == 'R':
            cols_start = cols_end - int(abs(cols_start-cols_end+1)/2)

    return {'row': rows_end, 'column': cols_end, 'seat_id': rows_end * 8 + cols_end}

def parse_file(name) -> list:
    lines = open(f'{os.path.dirname(__file__)}/{name}', 'r').read().splitlines()
    return lines

def test():
    assert parse_line('FBFBBFFRLR') == {'row': 44, 'column': 5, 'seat_id': 357}
    assert parse_line('BFFFBBFRRR') == {'row': 70, 'column': 7, 'seat_id': 567}
    assert parse_line('FFFBBBFRRR') == {'row': 14, 'column': 7, 'seat_id': 119}
    assert parse_line('BBFFBBFRLL') == {'row': 102, 'column': 4, 'seat_id': 820}

seats = [parse_line(x) for x in parse_file('input.txt')]
highest_id = max([x['seat_id'] for x in seats])
print(f'Part 1: {highest_id}')

seats.sort(key=lambda x: x['seat_id'])
current = seats[0]
for seat in seats[1:]:
    if current['seat_id'] + 1 == seat['seat_id']:
        current = seat
        continue
    else:
        my_seat = current['seat_id'] + 1
        break

print(f'Part 2: {my_seat}')

