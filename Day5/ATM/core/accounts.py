import os,sys,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Conf import Settings
from core import db_handler
'''
用于在文件里面加载和存贮账户数据
'''

import time ,json
def load_current_balence(accont_id):
    '''
    返回账户余额和其他基础信息
    :param accont_id: 用户账户的名字
    :return: 最新读取到的数据文件中的最新数据
    '''
    db_api = db_handler.db_handle()
    date = db_api("select * from accounts where account = %s" %accont_id) # 操作前再读取一边数据(保证数据是最新的)
    return  date

#写入文件数据
def dump_date(account_date):
    db_api = db_handler.db_handle()
    date = db_api("update accounts where account = %s" % account_date['id'],
                  account_date = account_date)
    return True

