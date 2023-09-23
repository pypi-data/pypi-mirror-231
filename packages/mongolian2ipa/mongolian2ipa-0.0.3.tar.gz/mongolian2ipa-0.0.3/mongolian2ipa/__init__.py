from mongolian2ipa.char_convertor import a_convert, w_convert, k_convert, o_convert, ou_convert, u_convert, oo_convert, \
    h_convert, e_convert, yu_convert, ye_convert, ya_convert, ii_convert, l_convert
from mongolian2ipa.mongolia_ipa_dictionary import mongolian_to_ipa


def mongolian2ipa(text: str) -> str:
    text = text.lower()

    ipa_transcription = ''

    for i in range(len(text)):
        c = text[i]

        try:
            add_char = None

            if c == 'а':
                add_char = a_convert(text, i)

            if c == 'в':
                add_char = w_convert(text, i)

            if c == 'г':
                add_char = k_convert(text, i)

            if c == 'й':
                add_char = ''

            if c == 'о':
                add_char = o_convert(text, i)

            if c == 'ө':
                add_char = ou_convert(text, i)

            if c == 'у':
                add_char = u_convert(text, i)

            if c == 'ү':
                add_char = oo_convert(text, i)

            if c == 'х':
                add_char = h_convert(text, i)

            if c == 'э':
                add_char = e_convert(text, i)

            if c == 'ю':
                add_char = yu_convert(text)

            if c == 'е':
                add_char = ye_convert(text, i)

            if c == 'я':
                add_char = ya_convert(text, i)

            if c == 'и':
                add_char = ii_convert(text, i)

            if c == 'л':
                add_char = l_convert(text, i)

            # ignore characters:
            if c in ['й', 'ь', 'ъ']:
                add_char = ''

            if add_char is not None:
                ipa_transcription += add_char
            else:
                ipa_transcription += mongolian_to_ipa[c]
        except KeyError:
            ipa_transcription += c

    return ipa_transcription
