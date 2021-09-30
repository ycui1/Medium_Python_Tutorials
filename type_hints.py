current_year = 2022


def formatted_age(person, birth_year):
    return f"{person}: {current_year - birth_year} years old"


formatted_age()


def formatted_age_typed(person: str, birth_year: int) -> str:
    return f"{person}: {current_year - birth_year} years old"


formatted_age_typed()