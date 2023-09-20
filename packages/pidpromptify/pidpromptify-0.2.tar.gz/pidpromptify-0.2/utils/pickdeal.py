import unicodedata
import regex as re
from pyvi import ViTokenizer, ViPosTagger
import pandas as pd
from promptify import Prompter, OpenAI

bang_nguyen_am = [['a', 'à', 'á', 'ả', 'ã', 'ạ', 'a'],
                  ['ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'aw'],
                  ['â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'aa'],
                  ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'e'],
                  ['ê', 'ề', 'ế', 'ể', 'ễ', 'ệ', 'ee'],
                  ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị', 'i'],
                  ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'o'],
                  ['ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'oo'],
                  ['ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ', 'ow'],
                  ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'u'],
                  ['ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự', 'uw'],
                  ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ', 'y']]

bang_ky_tu_dau = ['', 'f', 's', 'r', 'x', 'j']
nguyen_am_to_ids = {}

for i in range(len(bang_nguyen_am)):
    for j in range(len(bang_nguyen_am[i]) - 1):
        nguyen_am_to_ids[bang_nguyen_am[i][j]] = (i, j)


# Chuẩn hóa unicode
# Có 2 loại unicode : unicode tổ hơp và unicode dựng sẵn, điêu này dẫn tới việc 2 từ giống nhau sẽ bị coi là khác nhau
# Chuẩn hóa tất cả về 1 loại là unicode dựng sẵn
def chuan_hoa_unicode(text):
    text = unicodedata.normalize('NFC', text)
    return text


def chuan_hoa_dau_tu_tieng_viet(word):
    if not is_valid_vietnam_word(word):
        return word

    chars = list(word)
    dau_cau = 0
    nguyen_am_index = []
    qu_or_gi = False
    for index, char in enumerate(chars):
        x, y = nguyen_am_to_ids.get(char, (-1, -1))
        if x == -1:
            continue
        elif x == 9:  # check qu
            if index != 0 and chars[index - 1] == 'q':
                chars[index] = 'u'
                qu_or_gi = True
        elif x == 5:  # check gi
            if index != 0 and chars[index - 1] == 'g':
                chars[index] = 'i'
                qu_or_gi = True
        if y != 0:
            dau_cau = y
            chars[index] = bang_nguyen_am[x][0]
        if not qu_or_gi or index != 1:
            nguyen_am_index.append(index)
    if len(nguyen_am_index) < 2:
        if qu_or_gi:
            if len(chars) == 2:
                x, y = nguyen_am_to_ids.get(chars[1])
                chars[1] = bang_nguyen_am[x][dau_cau]
            else:
                x, y = nguyen_am_to_ids.get(chars[2], (-1, -1))
                if x != -1:
                    chars[2] = bang_nguyen_am[x][dau_cau]
                else:
                    chars[1] = bang_nguyen_am[5][dau_cau] if chars[1] == 'i' else bang_nguyen_am[9][dau_cau]
            return ''.join(chars)
        return word

    for index in nguyen_am_index:
        x, y = nguyen_am_to_ids[chars[index]]
        if x == 4 or x == 8:  # ê, ơ
            chars[index] = bang_nguyen_am[x][dau_cau]
            return ''.join(chars)

    if len(nguyen_am_index) == 2:
        if nguyen_am_index[-1] == len(chars) - 1:
            x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
            chars[nguyen_am_index[0]] = bang_nguyen_am[x][dau_cau]
        else:
            x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
            chars[nguyen_am_index[1]] = bang_nguyen_am[x][dau_cau]
    else:
        x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
        chars[nguyen_am_index[1]] = bang_nguyen_am[x][dau_cau]
    return ''.join(chars)


def is_valid_vietnam_word(word):
    chars = list(word)
    nguyen_am_index = -1
    for index, char in enumerate(chars):
        x, y = nguyen_am_to_ids.get(char, (-1, -1))
        if x != -1:
            if nguyen_am_index == -1:
                nguyen_am_index = index
            else:
                if index - nguyen_am_index != 1:
                    return False
                nguyen_am_index = index
    return True


def chuan_hoa_dau_cau_tieng_viet(sentence):
    """
        Chuyển câu tiếng việt về chuẩn gõ dấu kiểu cũ.
        :param sentence:
        :return:
        """
    sentence = sentence.lower()
    words = sentence.split()
    for index, word in enumerate(words):
        # cw = re.sub(r'(^\p{P}*)([p{L}]*\p{L}+)(\p{P}*$)', r'\1\2/\3', word).split('/')
        cw = re.sub(r'(^p{P}*)([p{L}.]*p{L}+)(p{P}*$)', r'1/2/3', word).split('/')
        # print(cw)
        if len(cw) == 3:
            cw[1] = chuan_hoa_dau_tu_tieng_viet(cw[1])
        words[index] = ''.join(cw)
    return ' '.join(words)


def chuan_hoa_date(sentence):
    def chuan_hoa_date(sentence):
        modified_text = re.sub(r'(\d{1,2})/(\d{1,2})(/(\d{1, 6}))?', r'\1.\2\3', sentence)
        return modified_text

    def change_date_format(sentence):
        modified_sentence = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\1.\2.\3', sentence)
        return modified_sentence

    modified_sentence = change_date_format(sentence)
    modified_sentence = chuan_hoa_date(modified_sentence)
    return modified_sentence


# Tách từ tiếng việt, từ tiếng việt không giống như tiếng anh, tách từ tiếng anh ta chỉ cần tách bằng khoảng trắng
# Tuy nhiên từ tiếng Việt có cả từ đơn lẫn từ ghép nên tách từ tiêng Việt sẽ phúc tạp hơn
# Project sử dung thu viện pyvi (xem mã nguồn tại : https://github.com/trungtv/pyvi) để phục vụ bài toán con tách từ Tiếng Việt
def tach_tu_tieng_viet(text):
    text = ViTokenizer.tokenize(text)
    return text


# Đưa về chữ viết thường
def chuyen_chu_thuong(text):
    return text.lower()


# Xóa đi các dấu cách thừa, các từ không cần thiết cho việc phân loại vẳn bản
def chuan_hoa_cau(text):
    text = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_.-]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def remove_special_tokens(sentence):
    cleaned_string = re.sub(r'\\[n|t]', ' ', sentence)
    json_data = cleaned_string.replace("'", "\"")
    # result = json.dumps(json_data, ensure_ascii=False)
    # json_data = json.loads(json_string)
    return json_data


def tien_xu_li(text):
    text = chuan_hoa_unicode(text)
    text = chuan_hoa_date(text)
    text = chuan_hoa_dau_cau_tieng_viet(text)
    text = tach_tu_tieng_viet(text)
    text = chuyen_chu_thuong(text)
    text = chuan_hoa_cau(text)
    return text


def read_data(file):
    data = pd.read_csv(file)
    data["processed_text"] = data["text"].apply(tien_xu_li)
    return data


class PickDealPromptify:
    def __init__(self, openai_key):
        self.openai_key = openai_key
        self.model = OpenAI(openai_key, model="gpt-3.5-turbo")
        self.prompter = Prompter(self.model)
        self.num_sent = 40
        self.temperature = 0.1
        self.labels = [
            "date",
            "trademark",
            "location",
        ]

    def __call__(self, path_file_jinja, sentence, *args, **kwargs):
        response_text = self.prompter.fit(path_file_jinja,
                                          text_input=sentence,
                                          labels=self.labels,
                                          domain="discount",
                                          num_sent=self.num_sent,
                                          temperature=self.temperature)["text"]
        result = remove_special_tokens(response_text)
        return result
