import os
from subprocess import call

GITEE_NAME = os.environ["GITEE_NAME"]
GITEE_EMAIL = os.environ["GITEE_EMAIL"]
GITEE_PATH = os.environ["GITEE_PATH"]

print("GITEE_NAME:", GITEE_NAME, ",GITEE_EMAIL:", GITEE_EMAIL)
print("GITEE_PATH:", GITEE_PATH)


def doGit(args):
    print("git", args)
    call('git', args)


# 设置邮箱等配置
cmd_list = [
    "config --local user.name \"{0}\"".format(GITEE_NAME),
    "config --local user.email \"{0}\"".format(GITEE_EMAIL), 
    "config --list"
]

for cmd in cmd_list:
    doGit(cmd)
