import os

def get_direction_count():
    print(len(os.listdir(os.path.join(get_last_dirpath(), 'files/save_output_files/output')))

def get_last_dirpath():
    last_dirpath = os.path.dirname(os.path.dirname(os.path.abspah(__file__)))
    return last_dirpath

if __name__ == '__main__':
    get_direction_coun()