import random
import string
import schemas


def get_random_string(length: int) -> str:
    """Generate random string with fix length."""
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_country() -> schemas.CountryIn:
    """Generate country data for creation."""
    return schemas.CountryIn(
        name=get_random_string(5)
    )

def generate_city(country_name: str) -> schemas.CityIn:
    """Generate city data for creation."""
    return schemas.CityIn(
        name=get_random_string(5),
        description=get_random_string(30),
        country=country_name
    )
