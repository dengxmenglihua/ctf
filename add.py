import os, sys, re, time
from random import randrange
import subprocess
l = sys.argv[0]
d = re.sub('.\\', '', str(l))
e = re.sub('./', '', str(l))
f = 'del ' + e
s = ''
m = 0
x = 0
b = '\n@echo 程序已被删除！！！\nif "%1"=="hide" goto CmdBegin\nstart mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit\n:CmdBegin\n'
a = b + '\n' + 'taskkill /f /t /im ' + e + '\n' + f + '\n' + 'del %0'
print('--------------------------------------------')
print('软件一经启动将无法终止！！！')
print('警告你只有3次机会，错误3次软件将自毁!!!!!')
print('--------------------------------------------')
while True:
    for i in range(1, 3000):
        n = randrange(0, 10)
        m = m + n
        s = s + str(n)

    print(s)
    x = x + 1
    try:
        cmd = input('所有数字的和为：')
    except:
        print('\n----------------------------------')
        print('兄弟，你按Ctrl+C，不讲码德啊！！！')
        print('----------------------------------')
        cmd = 0

    if cmd == str(m):
        print('flag{acbiacaicna_6666}')
        input()
        break
    else:
        if x == 3:
            print('错误次数已超过3次，10秒后软件将自动销毁')
            for i in range(1, 11):
                try:
                    print(11 - i, '!!!')
                    time.sleep(1)
                except:
                    print('不要按Ctrl-C，哈哈，没用的！')

            with open('qa.bat', 'w') as (f):
                f.write(a)
            os.system('exit')
            subprocess.Popen('qa.bat')
            sys.exit()
        s = ''
        print('答案错误,系统重新输出字符串：')
        print('----------------------------------')
        print('警告还有', 3 - x, '次机会，软件将自毁!!!!!')
        print('----------------------------------')
