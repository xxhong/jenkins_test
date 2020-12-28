import requests
import json
import os
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text
txt1 = execCmd('git rev-parse HEAD')
print("txt1:"+txt1)
gitTxt = str("git log --pretty=format:%s") +str(txt1)+ str(" -1")
print("gitTxt:[[[["+gitTxt)
print("str():"+str("%s"))
txt2 = execCmd(gitTxt)

print("最后文本:  [[[["+txt2+"】】】】")
headers = {'Content-Type': 'application/json'}
jsonData ={"msg_type": "text","content":{"text":txt2}};
feiShuUrl='https://open.feishu.cn/open-apis/bot/v2/hook/3f368105-c7e9-474c-9c94-f3d7b4ea7ef8'
r = requests.post(url=feiShuUrl, headers=headers,data=json.dumps(jsonData))
print(r)