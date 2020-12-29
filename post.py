import requests
import json
import os
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


id = execCmd("git rev-parse HEAD");
gitTxt = str('git log --pretty=format:"%s" ') + id[0:7] + str(" -1")
commitTxt = execCmd(gitTxt)
print("最后提交的内容：" + commitTxt)
headers = {'Content-Type': 'application/json'}
jsonData = {"msg_type": "text", "content": {"text": commitTxt}};
feiShuUrl = 'https://open.feishu.cn/open-apis/bot/v2/hook/3f368105-c7e9-474c-9c94-f3d7b4ea7ef8'
r = requests.post(url=feiShuUrl, headers=headers, data=json.dumps(jsonData))
