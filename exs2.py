def gears(data, n, m):
    suitable = n/m
    
    for box in data:
        for gear_wheel in box:
            if gear_wheel == 0:
                continue

            s = gear_wheel * suitable

            if s in box:

                return int(s), gear_wheel

    return None, None

print(gears([[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]], 30, 7))
