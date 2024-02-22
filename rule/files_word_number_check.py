import os
import re
from collections import Counter

class TextWordNumberCheck:

  def check_text(self, text):
    if len(text) <= 100:
      print(f"文本字数过少，仅有 {len(text)} 字")
      return False

    return True

if __name__ == '__main__':
  text_word_number_check = TextWordNumberCheck()
  get_last_dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  directory = os.path.join(get_last_dirpath, "files/save_output_files/需求相关/all")
  files = os.listdir(directory)
  for file in files:
    file_path = os.path.join(directory, file)
    with open(file_path, 'r', encoding='utf-8) as f:
              text = f.read()
    check_result = text_word_number_check.check_text(text)
    if check_result:
        pass
    else:
      print("文件: %s" % file + '\n')
      os.remove(file_path)
