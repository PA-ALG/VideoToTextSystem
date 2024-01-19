from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import os
import logging
from utils import log_collector
import ray
# import threading

# ray.init()
logger = log_collector.Logger(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log/log.txt'))

class AudioParser:

    def __init__(self, audio_in, output_dir):
        self.audio_in = audio_in
        self.output_dir = output_dir
        self.inference_pipeline = pipeline(
            task=Tasks.auto_speech_recognition,
            model='C:\MyCode\model\.cache\modelscope\hub\damo\speech_paraformer-large-vad-punc-spk_asr_nat-zh-cn',
            model_revision='v0.0.2',
            vad_model='C:\MyCode\model\.cache\modelscope\hub\damo\speech_fsmn_vad_zh-cn-16k-common-pytorch',
            punc_model='C:\MyCode\model\.cache\modelscope\hub\damo\punc_ct-transformer_cn-en-common-vocab471067-large',
            output_dir=output_dir,
        )

    def parsing(self):
        rec_result = self.inference_pipeline(audio_in=self.audio_in, batch_size_token=5000, batch_size_token_threshold_s=40, max_single_segment_time=6000)
        print(rec_result)

def check(source_dir, objective_dir):
    if len(objective_dir) == len(source_dir):
        return True

    else:
        return False

# @ray.remote
def main(i):
    # 视频转文本
    parsed_files = os.listdir("files/split_audio/")
    for dir in [parsed_files[i]]:
        try:
            print("正在解析视频文件 %s" % dir)
            logger.collect("正在解析视频文件 %s" % dir, logging.INFO)
            file_dir = "files/split_audio/" + dir
            files_count = len(os.listdir(file_dir))
            if files_count == 1:
                file_path = os.path.join(file_dir, dir) + '.wav'
                print("文件路径: %s" % file_path)
                output_file_path = file_path.replace('split_audio', 'results').replace('.wav', '')
                # 视频转为文本
                ap = AudioParser(file_path, output_file_path)
                ap.parsing()
            else:
                for i in range(1, files_count + 1):
                    try:
                        file_path = os.path.join(file_dir, dir) + '_split_' + str(i) + '.wav'
                        print("文件路径: %s" % file_path)
                        output_file_path = file_path.replace('split_audio', 'results').replace('.wav', '')
                        # 视频转为文本
                        ap = AudioParser(file_path, output_file_path)
                        ap.parsing()
                    except Exception as e:
                        pirint("%s 可能原因：视频片段没有声音。文件路径： %s" % (e, file_path))
                        logger.collect("%s 可能原因：视频片段没有声音。文件路径： %s" % (e, file_path), logging.WARNING)
                print("解析视频文件 %s 已完成" % dir, logging.INFO)
                logger.collect("解析视频文件 %s 已完成" % dir, logging.INFO)
                check_result = check('files/split_audio' + dir, 'files/results/' + dir)
                if check_result:
                    print("视频文件 %s 解析完整" % dir, logging.INFO)
                    logger.collect("视频文件 %s 解析完整" % dir, logging.INFO)
                else:
                    print("视频文件 %s 解析不完整，系统将自动删除。" % dir)
                    logger.collect("视频文件 %s 解析不完整，系统将自动删除。" % dir, logging.INFO)
                    os.remove('files/results/' + dir)
        except Exception as e:
            logger.collect("解析视频 %s 时报错,报错原因是L %s" % (dir, e), logging.ERROR)
            print(e)

if __name__ == '__main__':
    results = ray.get([main.remote(i) for i in range(4)])
    print(results)
    # thread1 = threading.Thread(target=main, args=(0,))
    # thread2 = threading.Thread(target=main, args=(1,))
    # thread3 = threading.Thread(target=main, args=(2,))
    # thread4 = threading.Thread(target=main, args=(3,))
    #
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    #
    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()
