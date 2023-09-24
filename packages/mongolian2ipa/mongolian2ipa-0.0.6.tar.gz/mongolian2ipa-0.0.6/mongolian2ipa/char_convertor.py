from mongolian2ipa.helpers import check_male_female_word, WordGender, vowels, check_first_level_vowel


# Characters functions
def a_convert(word: str, index: int) -> str:
    """
    а letter
    :param word:
    :param index:
    :return:
    """

    if not index == 0:
        if word[index - 1] in ['а', 'у']:
            return ''

    text = word[index:]

    is_ai = 'й' == text[1] if len(text) > 1 else False
    if is_ai:
        return 'æː'

    is_aa = 'а' == text[1] if len(text) > 1 else False

    # 'и', 'ь', 'ий'
    is_i = 'и' == text[2] if len(text) > 2 else False
    is_soft = 'ь' == text[2] if len(text) > 2 else False

    if is_aa:
        is_aa_i = 'и' == text[3] if len(text) > 3 else False
        is_aa_soft = 'ь' == text[3] if len(text) > 3 else False

        if is_aa_i or is_aa_soft:
            return 'æː'
        else:
            return 'aː'

    if not check_first_level_vowel(word, index):
        return 'ə'

    if is_i or is_soft:
        return 'æ'

    return 'a'


def w_convert(word: str, index: int) -> str:
    """
     В letter
    :param word:
    :param index:
    :return:
    """

    if len(word) > index + 1:
        next_char = word[index + 1]

        if next_char == 'т' or next_char == 'ц' or next_char == 'ч':
            return 'ɸ'

    return 'w'


def g_convert(word: str, index: int) -> str:
    """
     Г letter
    :param word:
    :param index:
    :return:
    """

    gender = check_male_female_word(word)

    if gender == WordGender.MALE:
        if len(word) == index + 1:
            return 'k'

        if len(word) > index + 1:
            if word[index + 1] in 'сш':
                return 'k'

        # гүй
        if len(word) > index + 2:
            if word[index + 1] == 'ү' and word[index + 2] == 'й':
                return 'k'

        if len(word) > index + 1:
            if word[index + 1] in vowels:
                return 'q'

    return 'k'


def o_convert(word: str, index: int) -> str:
    """
    О letter
    :param word:
    :param index:
    :return:
    """
    if not index == 0:
        if word[index - 1] == 'о':
            return ''

    text = word[index:]

    is_ai = 'й' == text[1] if len(text) > 1 else False
    if is_ai:
        return 'œː'

    is_oo = 'о' == text[1] if len(text) > 1 else False

    if is_oo:
        # Check if the substring contains 'и', 'ь', or 'ий'
        is_i = 'и' == text[3] if len(text) > 3 else False
        is_soft = 'ь' == text[3] if len(text) > 3 else False

        if is_i or is_soft:
            return 'œː'
        else:
            return 'ɔː'
    else:
        if not check_first_level_vowel(word, index):
            return 'ə'
        
        is_i = 'и' == text[2] if len(text) > 2 else False
        is_soft = 'ь' == text[2] if len(text) > 2 else False

        if is_i or is_soft:
            return 'œ'

    return 'ɔ'


def ou_convert(word: str, index: int) -> str:
    """
    Ө letter
    :param word:
    :param index:
    :return:
    """
    if not index == 0:
        if word[index - 1] == 'ө':
            return ''

    if not check_first_level_vowel(word, index):
        return 'ə'

    text = word[index:]

    is_ui = 'ө' == text[1] if len(text) > 1 else False
    if is_ui:
        return 'өː'

    return 'ө'


def u_convert(word: str, index: int) -> str:
    """
    У letter
    :param word:
    :param index:
    :return:
    """

    if not index == 0:
        if word[index - 1] == 'у':
            return ''

    text = word[index:]

    is_ui = 'й' == text[1] if len(text) > 1 else False
    if is_ui:
        return 'oi'

    is_ua = 'а' == text[1] if len(text) > 1 else False
    if is_ua:
        is_uai = 'й' == text[2] if len(text) > 2 else False

        if is_uai:
            return 'wæː'

        return 'waː'

    is_uu = 'у' == text[1] if len(text) > 1 else False

    if is_uu:
        # Check if the substring contains 'и', 'ь', or 'ий'
        is_i = 'и' == text[3] if len(text) > 3 else False
        is_soft = 'ь' == text[3] if len(text) > 3 else False

        if is_i or is_soft:
            return 'ʏː'
        else:
            return 'oː'
    else:
        # Check if the substring contains 'и', 'ь', or 'ий'
        is_i = 'и' == text[2] if len(text) > 2 else False
        is_soft = 'ь' == text[2] if len(text) > 2 else False

        if is_i or is_soft:
            return 'ʏ'

    return 'o'


def oo_convert(word: str, index: int) -> str:
    """
    Ү letter
    :param word:
    :param index:
    :return:
    """

    if not index == 0:
        if word[index - 1] == 'ү':
            return ''

    text = word[index:]

    is_ooi = 'й' == text[1] if len(text) > 1 else False
    if is_ooi:
        return 'ui'

    is_oooo = 'ү' == text[1] if len(text) > 1 else False

    if is_oooo:
        return 'uː'

    return 'u'


def h_convert(word: str, index: int) -> str:
    """
    Х letter
    :param word:
    :param index:
    :return:
    """
    if not index == 0:
        if word[index - 1] == 'л':
            return ''

    gender = check_male_female_word(word)

    if gender == WordGender.MALE:
        if len(word) > index + 1:
            if not word[index + 1] in ['т', 'ц', 'ч']:
                return 'ꭓ'
        else:
            return 'ꭓ'

    return 'x'


def e_convert(word: str, index: int) -> str:
    """
    Э letter
    :param word:
    :param index:
    :return:
    """

    if not index == 0:
        if word[index - 1] == 'э':
            return ''

    if not check_first_level_vowel(word, index):
        return 'ə'

    text = word[index:]

    is_ei = 'й' == text[1] if len(text) > 1 else False
    if is_ei:
        return 'eː'

    is_ei = 'э' == text[1] if len(text) > 1 else False
    if is_ei:
        return 'eː'

    return 'e'


def yu_convert(word: str) -> str:
    gender = check_male_female_word(word)

    if gender == WordGender.MALE:
        return 'joː'
    else:
        return 'juː'


def ye_convert(word: str, index: int) -> str:
    """
    Е letter
    :param word:
    :param index:
    :return:
    """
    text = word[index]
    length = len(text)

    if not index == 0:
        if word[index - 1] in vowels:
            return 'jə'

    if not text.find('өө') == -1:
        return 'jө'

    if length > 2 and index + 1 < length and text[1] == 'ө':
        return 'jөː'

    if length > 2 and index + 1 < length and text[1] == 'э':
        return 'jeː'

    return 'je'


def ya_convert(word: str, index: int) -> str:
    """
    Я letter
    :param word:
    :param index:
    :return:
    """
    text = word[index:]
    length = len(text)

    if not index == 0:
        if word[index - 1] in vowels:
            return 'jə'

    if length > 2 and index + 2 < length and text[index + 2] == 'ь':
        return 'jæ'

    if length > 1:
        if index + 1 < length and text[index + 1] == 'й':
            return 'jæː'
        elif index + 1 < length and text[index + 1] == 'а':
            return 'jaː'

    return 'ja'


def yo_convert(word: str, index: int) -> str:
    """
    Ё letter
    :param word:
    :param index:
    :return:
    """

    if not index == 0:
        if word[index - 1] in vowels:
            return 'jə'

    text = word[index:]
    length = len(text)

    for c in text:
        if c in ['й', 'ь']:
            return 'jœ'

    if length > 2 and index + 1 < length and text[1] == 'о':
        return 'jɔː'
    else:
        return 'jɔ'


def ii_convert(word: str, index: int) -> str:
    text = word[index:]
    length = len(text)

    if not check_first_level_vowel(word, index):
        return 'ə'

    if length > 2 and index + 1 < length and text[1] == 'й':
        return 'iː'
    else:
        return 'i'


def l_convert(word: str, index: int) -> str:
    if not index == 0:
        if word[index - 1] in 'оё':
            return 'l'

    text = word[index:]
    length = len(text)

    if length > 2 and index + 1 < length and text[1] == 'х':
        return 'ɬʰ'

    return 'ɬ'


def n_convert(word: str, index: int) -> str:
    text = word[index:]
    length = len(text)

    if length > 2 and index + 1 < length and text[1] in 'хгсш':
        return 'ŋ'

    if len(word) - 1 == index:
        return 'ŋ'
    else:
        return 'n'
