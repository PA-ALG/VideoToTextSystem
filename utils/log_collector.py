import logging
import os

class Logger:

    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = self.default_logger()

    def default_logger(self):
        # 创建日志文件
        if not os.path.exists(self.log_file):
            open(self.log_file, 'w', encoding='utf-8')
        # 创建一个logger
        logger = logging.getLogger('LogCollector')
        logger.setLevel(logging.DEBUG) # 设置日志级别
        # 创建一个文件处理器, 将日志写入指定的文件中
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)
        # 创建一个控制台处理器, 将日志输出到控制台上
        console_handler = logging.StreamHandler()
        console_handler.setLevel
        # 创建一个日志格式器, 并添加奥处理器中
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        # 将处理器添加到logger中
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        return logger

    def collect(self, message, level=logging.INFO):
        self.logger.log(level, message)

if __name__ == '__main__':
    log_collector = Logger(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log/log.txt'))
    log_collector.collect('This is a debug message', logging.DEBUG)
    log_collector.collect('This is a debug message', logging.INFO)
    log_collector.collect('This is a debug message', logging.WARNING)
    log_collector.collect('This is a debug message', logging.ERROR)
    log_collector.collect('This is a debug message', logging.CRITICAL)

