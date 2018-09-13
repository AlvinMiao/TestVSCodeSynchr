# -*- Coding:utf-8 -*-

# 数据库连接引擎
# 处理所有数据交互

import json, time, os, sys

# 导入环境变量路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from Conf import Settings


# 解析文件数据路径
def file_db_handle(conn_params):
    '''
    解析数据库文件路劲
    :return:
    '''
    return file_executes


def db_handle():
    '''
    连接数据库
    :return:
    '''
    # 把Settings下的DataBase的数据给conn_params
    conn_params = Settings.Database

    # 判断数据文件的类型
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
        pass # 提供一个可扩展接口


# 文件执行
def file_executes(sql, **kwargs):
    '''
    传入sql语句及其他变量
    :param sql:sql语句操作得到结果
    :return:
    '''
    conn_params = Settings.Database #二次赋值，意味着得到新的数据
    db_path = '%s%s' % (conn_params['path'], conn_params['name']) #得到数据文件的文件名和文件位置
    # sql = select * from accounts where account = %s % accounts
    sql_list = sql.split('where') #
    if sql_list[0].startswith('select') and len(sql_list) > 1:
        column, val = sql_list[1].strip().split('=')
        if column == 'acocunt':
            account_file = '%s/%s.json' % (db_path,val) # 得到数据文件的绝对路劲
            if os.path.isfile('account_file'):
                with open(account_file,'r') as Account_f:
                    account_data = json.load(Account_f) # json序列化，将数据进行赋值
                    return account_data
            else:
                exit("[%s]账户不存在！！！" % val)

            # 写入数据
        elif sql_list[0].startswith('update') and len(sql_list) > 1:
            column,val = sql_list[1].strip().split('=') # 剂啊昂账户写入到val里面去
            if column == 'account':
                account_file = '%s/%s.json' % (db_path,val)
                account_data = kwargs.get("account_data") # 得到账户数据
                with open(account_file,'w') as Ac_f:
                    acc_data = json.dump(account_data,Ac_f)
                    return  True

