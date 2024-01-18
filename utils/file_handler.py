import os

class FileHandler:

    def __init__(self):
        if not os.path.exits(os.path.join(slef.get_last_dirpath(), 'output')):
            os.mkdir(os.path.join(self.get_last_dirpath(), 'output')

    def merge_files(self, dir_path="results"):
        root_path = os.path.join(self.get_last_dirpath(), 'files/results')
        dirs = os.listdir(root_path)
        for dir in dirs:
            try:
                dir_path = dir_path + dir + "/"
                file_dir = os.listdir(dir_path)
                count = len(file_dir)
                if count == 1:
                    with open(os.path.join(self.get_last_dirpath(), 'files/results') + '/' + dir + '/' + dir + '/1best_recog/text_with_punc', 'r',
                              encoding='utf-8') as f:
                        data = f.read().replace(dir, '').replace('\n', '').replace(' ', '')
                    with open('../output/' + dir + '.txt', 'a', encoding='utf-8') as f:
                        f.write(data)
                elif count > 1:
                    for i in range(1, count + 1):
                        with open(os.path.join(self.get_last_dirpath(), 'files/results') + '/' + dir + '/' + dir + f'_split_{i}' + '/1best_recog/text_with_punc', 'r',
                                  encoding='utf-8') as f:
                            data = f.read().replace(dir + f'_split_{i}', '').replace('\n', '').replace(' ', '')
                        with open('../output/' + dir + '.txt', 'a', encoding='utf-8') as f:
                            f.write(data)
            except Exception as e:
                print(e)

    def get_last_dirpath(self):
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    file_handler = FileHandler()
    file_handler.merge_files