
a = ["www.abc.com","www.efg.com"]
urls = []
with open('E:/Python_Test/noval_email/noval.txt', 'r') as f:
    for line in f.readlines():
        if line != '\n':
            urls.append(line.strip())# 把末尾的'\n'删掉

print(urls)