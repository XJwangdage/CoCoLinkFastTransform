import re
while(True):
    id = re.search(r'\d+'， input("请输入作品ID或链接 > "))
    if id:
        id = id.group()
        print(f'社区链:\thttps://shequ.codemao.cn/work/{id}\nH5链:\thttps://coco.codemao.cn/editor/player/{id}?channel=h5\n社区iframe链:\thttps://coco.codemao.cn/editor/player/{id}?channel=community\n编辑器链:\thttps://coco.codemao.cn/editor/?workId={id}')
    else:
        print("输入格式有误")
