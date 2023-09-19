import sys
import re, os
import urllib.parse

try:
    appdatapath = os.environ['APPDATA'] or os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming')
    pippath = os.path.join(appdatapath, 'pip')
    pipfile = os.path.join(pippath, 'pip.ini')
    if not os.path.isdir(pippath):
        os.mkdir(pippath)
except:
    import traceback
    traceback.print_exc()

diclist = [
    ['http://pypi.tuna.tsinghua.edu.cn/simple/', '清华大学'],
    ['http://pypi.douban.com/simple/', '豆瓣'],
    ['http://mirrors.aliyun.com/pypi/simple/', '阿里云'],
    ['http://pypi.mirrors.ustc.edu.cn/simple/', '中国科学技术大学'],
]
dic_url2name = {}
dic_name2url = {}
for k,v in diclist:
    dic_url2name[k] = v
    dic_name2url[v] = k

def read_setting():
    if not os.path.isfile(pipfile):
        return None
    else:
        with open(pipfile) as f:
            setstr = f.read()
        mirrors = re.findall('\nmirrors = ([^\n]+)', setstr)[0]
        return dic_url2name.get(mirrors)

def write_setting(name=None):
    print('[pypi] change:', name or '默认')
    setting = '''[global]\nindex-url = {}\n[install]\nuse-mirrors = true\nmirrors = {}\ntrusted-host = {}'''.strip()
    if name is None:
        if os.path.isfile(pipfile):
            os.remove(pipfile)
        return
    if name not in dic_name2url:
        raise Exception("{} must in {}".format(name, list(dic_name2url)))
    mirrors = dic_name2url.get(name)
    index_url = mirrors.strip(' /')
    trusted_host = urllib.parse.urlsplit(index_url).netloc
    with open(pipfile, 'w') as f:
        f.write(setting.format(index_url, mirrors, trusted_host))


def install_all():
    inderer = 0
    changes = []
    changed = {}
    changed[inderer] = ['pypi', ['默认', None], [None], write_setting]
    changes.append([inderer, *changed[inderer]])
    inderer += 1
    for k, v in diclist:
        params = [v]
        info = [v, k]
        changed[inderer] = ['pypi', info, params, write_setting]
        changes.append([inderer, *changed[inderer]])
        inderer += 1
    return [changes, changed]

allsrcs, allsrcd = install_all()

def install(changer=None):
    if changer is None:
        print('[install]: v_src install [number]')
        print('[pypi] curr:', read_setting())
        for idx, _type, _info, _params, _set in allsrcs:
            print('  [*] [{}]: {:2}'.format(_type, idx), _info)
        return
    _, _info, _params, _set = allsrcd.get(changer, [None, None, lambda a:a])
    _set(*_params)

def execute():
    argv = sys.argv
    print('v_src :::: [ {} ]'.format(' '.join(argv)))
    if len(argv) == 1:
        install()
        return
    if len(argv) > 1:
        if argv[1] == 'install':
            if len(argv) > 2:
                install(int(argv[2]))

if __name__ == '__main__':
    execute()
    # change(1)
    # read_setting()
    # write_setting('豆瓣')
    # v = read_setting()
    # print(v)