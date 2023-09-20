# -*- coding: utf-8 -*-

from icu import BreakIterator, Locale

from tokenizers import pre_tokenizers


class UnicodeTokenizer:
    def __init__(self, lang="zh"):
        self.lang = lang
        self.word_breaker = BreakIterator.createWordInstance(Locale(lang))
        self.sentence_breaker = BreakIterator.createSentenceInstance(Locale(lang))
        self.pre_tokenizer = pre_tokenizers.Sequence([pre_tokenizers.Punctuation(), pre_tokenizers.Split(" ?[^(\\s|[.,!?…。，、।۔،])]+", "isolated"), pre_tokenizers.UnicodeScripts()])

    def split_lines(self, text):
        self.sentence_breaker.setText(text)
        parts = []
        p0 = 0
        for p1 in self.sentence_breaker:
            part = text[p0:p1]
            parts.append(part)
            p0 = p1
        return parts

    def tokenize(self, text):
        tokens = []
        lines = self.split_lines(text)
        for line in lines:
            spans = self.pre_tokenizer.pre_tokenize_str(line)
            for span, bound in spans:
                tokens += self.tokenize_line(span)
        return tokens

    def tokenize_line(self, line):
        self.word_breaker.setText(line)
        parts = []
        p0 = 0
        for p1 in self.word_breaker:
            part = line[p0:p1]
            parts.append(part)
            p0 = p1
        return parts


def demo_token():
    doc = [
        "'〇㎡[คุณจะจัดพิธีแต่งงานเมื่อไรคะัีิ์ื็ํึ]Ⅷpays-g[ran]d-blanc-élevé » (白高大夏國)😀熇'\x0000𧭏2022２０１９\U0010ffff",
        "대한민국의Ⅷ首先8.88设置 st。art_new_word=True 和 output=[açaí]，output 就是最终 no such name",
        "的输出คุณจะจัดพิธีแต่งงานเมื่อไรคะ탑승 수속해야pneumonoultramicroscopicsilicovolcanoconiosis",
        "하는데 카운터가 어디에 있어요ꆃꎭꆈꌠꊨꏦꏲꅉꆅꉚꅉꋍꂷꂶꌠلأحياء تمارين تتطلب من [MASK] [PAD] [CLS][SEP]",
        """est 𗴂𗹭𘜶𗴲𗂧, ou "phiow-bjij-lhjij-lhjij", ce que l'on peut traduire par « pays-grand-blanc-élevé » (白高大夏國).""",
        "วรรณพงษ์เป็นนักศึกษาชั้นปีที่หนึ่ง เรียนสาขาวิทยาการคอมพิวเตอร์และสารสนเทศคณะวิทยาศาสตร์ประยุกต์และวิศวกรรมศาสตร์อยู่ที่มหาวิทยาลัยขอนแก่นวิทยาเขตหนองคายยืมคืนทรัพยากรห้องสมุดเอกสารสัมมนาคอมพิวเตอร์ปัญญาประดิษฐ์กับการพัฒนาเกมแมวกินปลาหิวววไหมหลักสูตรใหม่สดสดทนได้",
        "ສົມເດັດພະເຈົ້າຢູ່ຫົວບໍຣົມໂກດຊົງທຳນຸບຳລຸງບ້ານເມືອງແລະພະສາດສະໜາຈົນກ່າວໄດ້ວ່າກຸງສີອະຍຸທະຢາໃນສະໄໝພະອົງນັ້ນເປັນຍຸກທີ່ບ້ານເມືອງດີ ມີຂຸນນາງຄົນສຳຄັນທີ່ເຕີບໂຕໃນເວລາຕໍ່ມາ ໃນລາຊະການຂອງພະອົງຫຼາຍຄົນ ເຊັ່ນ ສົມເດັດພະເຈົ້າກຸງທົນບຸລີ, ພະບາດສົມເດັດພະພຸດທະຍອດຟ້າຈຸລາໂລກມະຫາລາດ ເປັນຕົ້ນ ໃນທາງດ້ານວັນນະຄະດີກໍມີກະວີຄົນສຳຄັນ ເຊັ່ນ ເຈົ້າຟ້າທຳມາທິເບດໄຊຍະເຊດສຸລິຍະວົງ ກົມມະຂຸນເສນາພິທັກ ຫຼືເຈົ້າຟ້າກຸ້ງ ເຊິ່ງເປັນພະໂອລົດ ເປັນຕົ້ນ",
    ]
    tokenizer = UnicodeTokenizer()
    for line in doc:
        print(tokenizer.split_lines(line))
        print(tokenizer.pre_tokenizer.pre_tokenize_str(line))
        print(tokenizer.tokenize_line(line))
        print(tokenizer.tokenize(line))



if __name__ == "__main__":
    demo_token()


