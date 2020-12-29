import requests
import json
import os
#终端执行
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text
#获取git最后一次提交的message
def getLastGitMsg():
    id = execCmd("git rev-parse HEAD");
    gitTxt = str('git log --pretty=format:"%s" ') + id[0:7] + str(" -1")
    commitTxt = execCmd(gitTxt)
    return commitTxt
#飞书通知
def postToFeishu(title,desc,downloadInfo):
    feiShuUrl = 'https://open.feishu.cn/open-apis/bot/v2/hook/3f368105-c7e9-474c-9c94-f3d7b4ea7ef8'
    headers = {'Content-Type': 'application/json'}
    jsonDataPost = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": title,
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": desc
                            },
                            {
                                "tag": "text",
                                "text": downloadInfo,
                            }
                        ]
                    ]
                }
            }
        }
    }
    requests.post(url=feiShuUrl, headers=headers, data=json.dumps(jsonDataPost))

lastGitMsg = getLastGitMsg()
buildPassword = "joy123" #蒲公英下载app的密码
_api_key = "317238dee35e41f3a4a44811d93ce456"
#上传apk到蒲公英
def uploadToPgyer(apk):
    uploadUrl = 'https://www.pgyer.com/apiv2/app/upload' #蒲公英api_key
    files = {'file': open(apk, 'rb')}
    data = {'_api_key': _api_key, 'buildPassword': buildPassword,"buildUpdateDescription":lastGitMsg,"buildInstallType":2}
    response = requests.post(uploadUrl, files=files, data=data)
    if response.status_code == 200 and response.json().get("code") == 0 :
        dataContent = response.json().get("data")
        buildShortcutUrl = dataContent.get("buildShortcutUrl")
        postToFeishu("Nonogram.ly Android 测试环境 发布成功!","版本说明: "+lastGitMsg,"\n下载地址： https://www.pgyer.com/"+buildShortcutUrl+" 密码:"+buildPassword);
        print("上传成功")
    else:
        print("上传失败")
apk='app/build/outputs/apk/debug/app-debug.apk'
uploadToPgyer(apk);
