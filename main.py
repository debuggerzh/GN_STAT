# 这是一个示例 Python 脚本。
from collections import Counter
from matplotlib import pyplot as plt
import matplotlib
import requests

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
translate = {
    '艾白_千鸟Official': '一只修白勾',
    '尼特Neet_Channel': '尼特Neet很不Official',
    '文静_千鸟Official': '明前奶绿',
    '艾瑞思_千鸟Official': '凜凜蝶凜',
}


def supply(ctr: Counter):
    ctr['尼特Neet很不Official'] += 1  # e01

    ctr['尼特Neet很不Official'] += 1
    ctr['尤娜_Official'] += 1  # e02

    ctr['尼特Neet很不Official'] += 1
    ctr['尤娜_Official'] += 1
    ctr['莉奥拉Liala'] += 1
    ctr['弥生月official'] += 1  # e03

    ctr['尼特Neet很不Official'] += 1
    ctr['尤娜_Official'] += 1
    ctr['莉奥拉Liala'] += 1
    ctr['一只修白勾'] += 1
    ctr['弥生月official'] += 1  # e04

    ctr['尼特Neet很不Official'] += 1
    ctr['尤娜_Official'] += 1
    ctr['莉奥拉Liala'] += 1
    ctr['一只修白勾'] += 1
    ctr['琳_千鸟Official'] += 1  # e06

    ctr['尼特Neet很不Official'] += 1
    ctr['尤娜_Official'] += 1
    ctr['神宫咲Saki'] += 1
    ctr['冰糖IO'] += 1
    ctr['明前奶绿'] += 1
    ctr['伊什纳Eithna'] += 1  # e08

    ctr['尼特Neet很不Official'] += 1
    ctr['一只修白勾'] += 1
    ctr['杜松子_Gin'] += 1
    ctr['竹月芽Meiya'] += 1
    ctr['梨安不迷路'] += 1  # e09

    ctr['尼特Neet很不Official'] += 1
    ctr['雪绘Yukie'] += 1
    ctr['神宫咲Saki'] += 1
    ctr['東雪蓮Official'] += 1
    ctr['帛未Bovei'] += 1
    ctr['冰糖IO'] += 1
    ctr['一只修白勾'] += 1  # e15

    ctr['尼特Neet很不Official'] += 1
    ctr['冰糖IO'] += 1
    ctr['安蒂维娜-克莱因'] += 1
    ctr['千春_Chiharu'] += 1
    ctr['琳_千鸟Official'] += 1
    ctr['一只修白勾'] += 1  # e38

    ctr['尼特Neet很不Official'] += 1
    ctr['咩栗'] += 1
    ctr['韶华依依Official'] += 1
    ctr['茉里Mari'] += 1
    ctr['言彦_SAY'] += 1
    ctr['诺娅Sukie'] += 1
    ctr['一只修白勾'] += 1  # e47

    ctr['咩栗'] += 1
    ctr['黎歌Neeko_channel'] += 1
    ctr['阿萨Aza'] += 1
    ctr['早稻叽'] += 1
    ctr['未未昭'] += 1
    ctr['一只修白勾'] += 1  # e76

    ctr['咩栗'] += 1
    ctr['呜米'] += 1
    ctr['麻尤米mayumi'] += 1
    ctr['瑞娅_Rhea'] += 1
    ctr['白神遥Haruka'] += 1
    ctr['有棵里里'] += 1
    ctr['勺Shaun'] += 1  # e121

    ctr['东爱璃Lovely'] += 1
    ctr['Ask是Asuka'] += 1
    ctr['惑姬Waku'] += 1
    ctr['未未昭'] += 1
    ctr['凜凜蝶凜'] += 1
    ctr['灯瑠hiru'] += 1
    ctr['千春_Chiharu'] += 1  # e133


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def get_comments(aid: int) -> int | str:
    """

    :param aid: av号
    :return: 表示本期主播信息的字符串
    """
    url = 'https://api.bilibili.com/x/v2/reply/main'
    query = {
        'next': None,
        'type': 1,
        'oid': aid,
        'mode': 3,
    }
    for i in range(1, 10):
        query['next'] = i
        resp = requests.get(url, params=query)
        json_data = resp.json()
        replies = json_data['data']['replies']
        if replies is None:
            return f'{aid}\n'
        for reply in replies:
            if reply['mid'] == 1827645033:
                return reply['content']['message'] + '\n'
        pass


def get_collection() -> list:
    aids = []
    url = 'https://api.bilibili.com/x/polymer/space/seasons_archives_list'
    query = {
        'mid': 1827645033,
        'season_id': 244622,
        'sort_reverse': 'false',
        'page_num': None,
        'page_size': 100,
    }
    for i in (1, 2):
        query['page_num'] = i
        # query_str = urlencode(query)
        resp = requests.get(url, params=query)
        json_data = resp.json()
        aids += json_data['data']['aids']
    return aids


def generate_metadata():
    with open('stat.txt', 'w', encoding='utf-8') as fp:
        for av in av_ids:
            fp.write(get_comments(av))
            print(f'{av} is recorded.')


def matplot_init():
    font = {
        'family': 'Microsoft YaHei',
        'weight': 'bold',
        'size': 12
    }
    matplotlib.rc("font", **font)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('BiliBili')
    av_ids = get_collection()
    print(len(av_ids))

    # print(get_comments(724562067))
    # generate_metadata()
    ctr = Counter()
    supply(ctr)
    with open('stat.txt', 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            if '：' in line:
                uploader = line.split('：')[0]
                if uploader in translate:
                    uploader = translate[uploader]
                ctr[uploader] += 1
            else:
                # print(line)
                ...

    top20 = ctr.most_common(20)
    print(top20)
    vtbs = [x[0] for x in top20]
    times = [x[1] for x in top20]
    print(vtbs, times)

    matplot_init()

    plt.figure(figsize=(16, 9))
    bar = plt.bar(vtbs, times)
    plt.bar_label(bar, label_type='edge')
    plt.xticks(range(20), vtbs, rotation=60)
    plt.subplots_adjust(top=0.95, bottom=0.2)
    # plt.show()
    plt.savefig('top20.png')
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
