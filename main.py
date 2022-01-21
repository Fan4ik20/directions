def direction(facing: str, turn: int) -> str:
    if not (-1080 <= turn <= 1080):
        raise ValueError('Turn value must be from -1080 to 1080 degrees!')
    if turn % 45 != 0:
        raise ValueError('Turn value must be a multiple of 45!')

    facing_degrees = {
        'N': 0,
        'NE': 45,
        'E': 90,
        'SE': 135,
        'S': 180,
        'SW': 225,
        'W': 270,
        'NW': 315,
    }

    if facing not in facing_degrees:
        raise ValueError(
            f'Facing must be one of: {list(facing_degrees.keys())}')

    # Get rid of working with negative
    # numbers and a range that differs from (0, 360).
    turn %= 360

    start_facing_degrees = facing_degrees[facing]

    new_facing_degrees = start_facing_degrees + turn

    new_facing = None
    for facing, degrees in facing_degrees.items():
        # We use modulo for 1 case - the if result is 360 degrees.
        if new_facing_degrees % 360 == degrees:
            new_facing = facing
            break

    return new_facing
