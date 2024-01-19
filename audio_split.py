import os
from moviepy.editor import AudioFileClip
import shutil
import logging
from utils import log_collector

logger = log_collector.Logger(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log/log.txt'))

class Splitter:

    def __init__(self):
        # 确保输出目录存在
        if not os.path.exists('files/split_audio/'):
            os.mkdir('files/split_audio/')

    def split_audio(self, input_file, output_dir,
                    split_duration=180):  # split_duration is in seconds, 5 minutes = 300 seconds
        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 读取音频文件
        audio_clip = AudioFileClip(input_file)
        # 获取音频的总时长（秒）
        audio_duration = audio_clip.duration
        if audio_duration > 180:
            # 计算分段的数量
            num_splits = (audio_duration + split_duration - 1) // split_duration
            # 遍历每个分段并保存
            for i in range(int(num_splits)):
                start_time = i * split_duration
                end_time = min((i + 1) * split_duration, audio_duration)
                # 提取分段
                subclip = audio_clip.subclip(start_time, end_time)
                # 构建输出文件名
                output_file = os.path.join(output_dir,
                                           f"{os.path.splitext(os.path.basename(input_file))[0]}_split_{i + 1}.wav")
                # 写入分段音频
                subclip.write_audiofile(output_file)
                print(f"保存音频片段 {i + 1}/{num_splits}: {output_file}")
                logger.collect(f"保存音频片段 {i + 1}/{num_splits}: {output_file}", logging.INFO)
            check_result = self.files_integrality_check(output_dir, num_splits)
            if check_result:
                print(f"所有 {num_splits} 音频片段文件被保存至 {output_dir}。")
                logger.collect(f"所有 {num_splits} 音频片段文件被保存至 {output_dir}。")
                return True

            else:
                print(f"{num_splits} 音频片段文件不是完整的, 系统将自动删除。")
                logger.collect(f"{num_solits} 音频片段文件不是完整的, 系统将自动删除", logging.ERROR)
                os.remove(output_dir)
                return False

        else:
            shutil.copy(input_file, output_dir)

    def files_integrality_check(self, file_path, nums):
        files_number = len(os.listdir(file_path))
        if files_number == nums:
            return True

        else:
            return False

if __name__ == '__main__':
    # 视频切割
    splitter = Splitter()
    convertered_files = os.listdir("files/output_audio/")
    for file in convertered_files:
        try:
            input_file = 'files/output_audio/%s' % file
            output_dir = ('files/split_audio/%s' % file).replace('.wav', '')
            splitter.split_audio(input_file, output_dir)
        except Exception as e:
            logger.collect(e, logging.ERROR)
            print(e)
