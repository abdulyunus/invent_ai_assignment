from datetime import datetime


def parse_date(x):
    """
    Attempts to parse a date string into a datetime object using multiple formats.

    Tries the following formats in order:
    1. "%m/%d/%Y" (e.g., 02/10/2015)
    2. "%d/%m/%Y" (e.g., 10/02/2015)
    3. "%Y-%m-%d" (e.g., 2015-02-10)

    Args:
        x: The input date string or value to parse.

    Returns:
        datetime: Parsed datetime object.

    Raises:
        ValueError: If none of the formats match the input.
    """
    try:
        return datetime.strptime(str(x), "%m/%d/%Y")
    except:
        try:
            return datetime.strptime(str(x), "%d/%m/%Y")
        except:
            return datetime.strptime(str(x), "%Y-%m-%d")
