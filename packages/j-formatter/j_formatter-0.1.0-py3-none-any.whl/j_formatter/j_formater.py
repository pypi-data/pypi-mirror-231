def convert_to_j_format(sec):
    """
    Function to return the seconds in JIRA like format.
    Parameters:
        sec : seconds
    Returns:
        Formatted seconds to JIRA like time format
        Example : "12w 2d 3h 21m"

    """
    seconds = int(sec)

    WEEK = 60 * 60 * 24 * 7
    DAY = 60 * 60 * 24
    HOUR = 60 * 60
    MINUTE = 60

    weeks = seconds // WEEK
    seconds = seconds % WEEK
    days = seconds // DAY
    seconds = seconds % DAY
    hours = seconds // HOUR
    seconds = seconds % HOUR
    minutes = seconds // MINUTE

    if weeks == 0 and days == 0:
        return f"{hours}h {minutes}m"

    if weeks == 0:
        return f"{days}d {hours}h {minutes}m"

    return f"{weeks}w {days}d {hours}h {minutes}m"