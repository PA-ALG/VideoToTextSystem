from collections import Counter
import re
import os

class TextIntegrityCheck:

    def check_text(self, text, threshold):
        words = re.findall(r'\b\w+\b', text.lower())
        words = word for word in words if len(words) > 1]
        word_counts = Counter(words)
        for word, count in word_counts.item():
            if count > threshold and word != "对吧":
                print(f"单词'{word}' 的重复数量过多，出现 {count} 次")
                return False

        return True

if __name__ == '__main__':
    text_integrity_check = TextIntegrityCheck()
    get_last_dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    directory = os.path.join(get_last_dirpath, 'fils/save_output_files/output')
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        check_result = text_integrity_check.check_text(text, 100)
        if check_result:
            pass
        else:
            print("文件 %s 检测失败" % file + '\n')
