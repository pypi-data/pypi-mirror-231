from enum import Enum

vowels = ['а', 'э', 'и', 'о', 'ө', 'ү', 'у']


class WordGender(Enum):
    MALE = 1
    FEMALE = 0


def check_male_female_word(word: str) -> WordGender:
    is_a = 'а' in word
    is_o = 'о' in word
    is_u = 'у' in word
    is_y = 'я' in word
    is_yu = 'ю' in word

    if is_a or is_o or is_u or is_y or is_yu:
        return WordGender.MALE

    is_e = 'э' in word
    is_oo = 'ө' in word
    is_uu = 'ү' in word

    if is_e or is_oo or is_uu:
        return WordGender.FEMALE

    return WordGender.FEMALE
