def remove_tailing_zeros(float_number):
    try:
        result = float_number.rstrip('0').rstrip(
            '.') if '.' in float_number else float_number
        return result
    except ValueError as e:
        raise ValueError(
            "Could not get '%f' as number: %f" % (float_number, e))
