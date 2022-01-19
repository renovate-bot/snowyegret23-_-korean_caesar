# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = [
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
]
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [
    " ",
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

# 출처: https://frhyme.github.io/python/python_korean_englished/
def korean_to_be_englished(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        if "가" <= w <= "힣":
            ch1 = (ord(w) - ord("가")) // 588
            ch2 = ((ord(w) - ord("가")) - (588 * ch1)) // 28
            ch3 = (ord(w) - ord("가")) - (588 * ch1) - 28 * ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst


def caesar(dist, number):
    word = korean_to_be_englished(dist)
    wordlist = []
    print(word[0])
    if len(word[0]) == 1:
        return word[0]
    elif len(word[0]) == 3 and word[0][2] != " ":
        for i in range(len(CHOSUNG_LIST)):
            if word[0][0] == CHOSUNG_LIST[i]:
                wordlist.append(CHOSUNG_LIST[i + number])
        wordlist.append(word[0][1])
        for k in range(len(JONGSUNG_LIST)):
            if word[0][2] == JONGSUNG_LIST[k]:
                wordlist.append(JONGSUNG_LIST[k + number])
    elif len(word[0]) == 3 and word[0][2] == " ":
        for i in range(len(CHOSUNG_LIST)):
            if word[0][0] == CHOSUNG_LIST[i]:
                wordlist.append(CHOSUNG_LIST[i + number])
        wordlist.append(word[0][1])
    return wordlist


def caesarPack(text, number):
    textlist = []
    for i in range(len(text)):
        textlist.append(caesar(text[i], number))
    return textlist


print(caesarPack("안녕하세요?", -3))
# >>> [['ㅃ', 'ㅏ', 'ㄱ'], ['ㅎ', 'ㅕ', 'ㅄ'], ['ㅋ', 'ㅏ'], ['ㅁ', 'ㅔ'], ['ㅃ', 'ㅛ'], ['?']]
