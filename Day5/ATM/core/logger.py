import logging,sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from Conf import Settings
'''
日志记录模块，处理所有日志工作
'''

def logger(log_type):
    '''
    创建日志
    :param log_type:
    :return:
    '''
    logger = logging.getLogger(log_type)
    logger.setLevel(Settings.Log_Level)

    #创建控制台处理程序并将级别设置为调试
    ch = logging.StreamHandler()
    ch.setLevel(Settings.Log_Level)

    #创建文件处理程序并将级别设定为警告
    log_file = "%s/logs/%s" %(BASE_DIR,Settings.Log_Types[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(Settings.Log_Level)

    #创建格式化程序
    formatter = logging.Formatter('%(asctime)s - %(names) - %(levename)s - %(messege)s')

    #添加格式化的ch和fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    #添加ch和fh到logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger