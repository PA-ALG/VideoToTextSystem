import os
from moviepy.editor import VideoFileClip
import shutil
import logging
from utils import log_collector

logger = log_collector.Logger(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log/log.txt'))

class AudioConverter:

    def __init__(self):
        if not os.path.exists('files/output_audio/'):
            os.mkdir('files/output_audio/')

    def trans_mp4_to_wav(self, mp4_file, wav_file):
        # 创建 VideoFileClip 对象
        clip = VideoFileClip(mp4_file)
        # 获取音频
        audio = clip.audio
        # 保存音频为 wav 格式
        audio.write_audiofile(wav_file)

    def check(self):
        source_video = os.listdir('files/videos/')
        object_video = os.listdir('files/output_audio/')
        source_video_count = len(os.listdir('files/videos/'))
        object_video_count = len(os.listdir('files/output_audio/'))
        if object_video_count == source_video_count:
            print("视频转码完成,且数量一致")
            logger.collect("视频转码完成,且数量一致", logging.INFO)
        else:
            failure_videos = [video for video in source_video_count not in source_video_count]
            print("视频转码完成,但数量不一致。原视频是 %d 个,转码后视频是 %d 个" % (source_video_count, object_video_count))
            logger.collect("视频转码完成,但数量不一致。原视频是 %d 个,转码后视频是 %d 个" % (source_video_count, object_video_count), logging.ERROR)
            print("转码失败的视频有: %s" % ",".join(failure_videos))
            logger.collect("转码失败的视频有: %s" % ",".join(failure_videos), logging.ERROR)

if __name__ == '__main__':
    # 视频转码
    audio_converter = AudioConverter()
    files = os.listdir("files/videos/")
    convertered_files = os.listdir("files/output_audio/")
    for file in files:
        try:
            # 若转后目录已存在相同文件则不转码
            if file.replace('mp4', 'wav') not in convertered_files:
                input_file = "files/videos/%s" % file
                output_file = "files/output_audio/%s" % file.replace('mp4', 'wav')
                file_extension = os.path.splitext(file)[1]
                if file_extension == ".mp4":
                    audio_converter.trans_mp4_to_wav(input_file, output_file)
                # 若存在wav文件则复制到转后目录
                elif file_extension == ".wav":
                    shutil.copy(input_file, output_file)
        except Exception as e:
            logger.collect(e, logging.ERROR)
            print(e)
