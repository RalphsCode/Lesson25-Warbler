<<<<<<< HEAD
"""Support functions for CSV generation."""

from datetime import datetime
from random import uniform


def get_random_datetime(year_gap=2):
    """Get a random datetime within the last few years."""

    now = datetime.now()
    then = now.replace(year=now.year - year_gap)
    random_timestamp = uniform(then.timestamp(), now.timestamp())

    return datetime.fromtimestamp(random_timestamp)
=======
"""Support functions for CSV generation."""

from datetime import datetime
from random import uniform


def get_random_datetime(year_gap=2):
    """Get a random datetime within the last few years."""

    now = datetime.now()
    then = now.replace(year=now.year - year_gap)
    random_timestamp = uniform(then.timestamp(), now.timestamp())

    return datetime.fromtimestamp(random_timestamp)
>>>>>>> e49aa515c47b4c229a972e7c93c1b38f00a062e4
