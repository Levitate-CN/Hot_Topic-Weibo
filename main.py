import requests
from tkinter import  *
url = 'https://weibo.com/ajax/statuses/hot_band'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70 '
}
response_dics = requests.get(url, headers).json()['data']['band_list']
news_all = []
raw_hot = []
for response in response_dics:

    try:
        rank = response['realpos']
        content = response['word']
        hot = response['raw_hot']

        news_all.append(content)
        raw_hot.append(hot)
    except KeyError:
        pass
def show():
    list_box1.delete(0,-1)
    for index,item in enumerate(news_all):
        content = '第'+str(index+1)+': ' +'热度'+ str(raw_hot[index]) + '      #内容:   '+item
        list_box1.insert(index,content)

root = Tk()
x = int((root.winfo_screenwidth() - 800) / 2)
y = int((root.winfo_screenheight() - 600) / 2)
root.geometry('800x600+%s+%s'%(x,y))
root.resizable(False, False)

l1 = Label(root,text='微博热搜',font=('微软雅黑', 15))
l1.grid(row=0,column=0)

list_box1 = Listbox(root,width=110,height=27)
list_box1.grid(row=1,column=0)

b1 = Button(root,text='查看热搜',width=100,command=show)
b1.grid(row=2,column=0)

s = Scrollbar(root,width=50)
s.grid(row=1,column=1,sticky=S + W + E + N,rowspan=1)
s.config(command=list_box1.yview)

root.mainloop()
