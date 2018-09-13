# 参数配置文件
# -*- Colding:utf-8 -*-
import os, sys, logging

# 导入自定义变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# print(Base_Dir)


Database = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR,
}

Log_Level = logging.INFO

# 用于记录日志
Log_Types = {
    'transaction': 'transacation.log',
    'access': 'access.log',
}
# 交易的配置类型
Transacation_Type = {
    'repay': {'action': 'plus', 'interest': 0},  # 还款
    'withdraw': {'action': 'minus', 'interest': 0.05},  # 取现，降低可用余额
    'transfer': {'action': 'minus', 'interest': 0.05},  # 提现，降低可用余额
    'consume': {'action': 'minus', 'interest': 0}
}
