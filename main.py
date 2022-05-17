# 主文件

import pysnowball as ball
from LimitUpAfterThreeDayWithDB import fetchLimitUpAfterThreeDay
from NineYin import nineDailyData, nineMonthlyData, nineWeeklyData
from Shareholder import topTenHolders, allHolders
from StockToDB import upgradeStockList, upgradeStockTrade
from utils import currentTime


def main():
    print('###初始化执行任务')
    print('[1] 保存并且更新股票信息')
    print('[2] 保存并且更新股票行情')
    print('[3] 全量更新')
    print('[4] 获取连日阴票')
    print('[5] 获取连周阴票')
    print('[6] 获取连月阴票')
    print('[7] 获取满足4天前涨停后3天不破位的票')
    print('[8] 获取股票股东信息')
    print('根据编号选择任务:')
    s = int(input())
    ball.set_token('xq_a_token=9d7c75c59c8b3ef763711f682f3bb26163c4aad7;')
    timestamp = currentTime()

    if s == 1:
        upgradeStockList(timestamp)
        print('\r保存并且更新股票信息,已完成！')
    elif s == 2:
        upgradeStockTrade(timestamp, 'daily')
        print('\r保存并且更新股票行情,已完成！')
    elif s == 3:
        upgradeStockList(timestamp)
        upgradeStockTrade(timestamp)
        print('\r全量更新,已完成！')
    elif s == 4:
        print('输入连阴次数:')
        count = int(input())
        if count <= 4:
            nineDailyData(4)
        elif count >= 9:
            nineDailyData(9)
        else:
            nineDailyData(count)
    elif s == 5:
        print('输入连阴次数:')
        count = int(input())
        if count <= 4:
            nineWeeklyData(4)
        elif count >= 9:
            nineWeeklyData(9)
        else:
            nineWeeklyData(count)
    elif s == 6:
        print('输入连阴次数:')
        count = int(input())
        if count <= 4:
            nineMonthlyData(4)
        elif count >= 9:
            nineMonthlyData(9)
        else:
            nineMonthlyData(count)
    elif s == 7:
        fetchLimitUpAfterThreeDay()
    elif s == 8:
        print('[1] 前十股东信息:')
        print('[2] 全部股东信息:')
        print('根据编号选择任务:')
        t = int(input())
        print('请输入股票编码(带上大写SZ或者SH):')
        code = str(input())
        if t == 1:
            topTenHolders(code)
        elif t == 2:
            allHolders(code)
        else:
            topTenHolders(code)
    else:
        print('输入错误。。。')


main()
