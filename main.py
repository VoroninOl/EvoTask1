

def direction(facing, turn):
    """ Returns your direction
    
    Keyword arguments:
    facing -- one of the 8 directions: N, NE, E, SE, S, SW, W, NW
    turn -- a multiple of 45, between -1080 and 1080
    """
    facing_in_degrees = {
        "N": 0, "NE": 45, "E": 90, "SE": 135,
        "S": 180, "SW": 225, "W": 270, "NW": 315
    }
    facing_in_letters = {
        facing_in_degrees[dir]: dir for dir in facing_in_degrees
    }
    try:
        start_direction = facing_in_degrees[facing]
    except Exception as ex:
        print('Mistake in start direction - {}'.format(ex))
        return
    finish_direction = start_direction + turn
    finish_direction = finish_direction % 360
    try:
        result = facing_in_letters[finish_direction]
    except Exception as ex:
        print('Mistake in turn - {}'.format(ex))
        return
    return result


