import os

# 更新
def update_svn(path):
    print("update ", path)
    cmd = f'svn update {path} --non-interactive --accept theirs-full '
    ret = os.system(cmd)

    print("resolve confilict ", path)
    cmd = f'svn resolve {path} --depth infinity --accept theirs-full  --non-interactive '
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("update Error!:"+path)


def commit_svn(path):
    commit_svn_comment(path, "auto commmit")


def revert_svn(path):
    command = f'''svn revert -R {path} '''
    ret = os.system(command)
    print(command)
    if ret != 0:
        raise Exception("revert Error!:"+path)
        return
    else:
        print("revert ok!")


def commit_svn_comment(path, comment):
    command = f'''svn ci {path} -m "{comment}" -q '''
    ret = os.system(command)
    print(command)
    if ret != 0: 
        raise Exception("commit Error!:"+path)
        return
    else:
        print("commit ok!")


def resolveConflict(path):
    cmd = 'svn status ' + path
    ret = os.popen(cmd)
    text = ret.read()
    ret.close()
    for linetext in text.splitlines():
        wordlist = re.split(r'\s+', linetext)
        print(wordlist)
        if len(wordlist) >= 2 and wordlist[0] == "C":
            filepath = os.path.join(path, wordlist[1])
            cmd = 'svn resolve ' + filepath + '--accept theirs-full  --non-interactive '
            ret = os.system(cmd)
            print("resolve confilict ok ", path)


def add_svn(path):
    cur_path = os.getcwd()
    # 当前文件目录
    os.chdir(path)
    command = '''svn status|grep ? |awk '{print($2}'|xargs svn add'''
    ret = os.system(command)
    print(command)
    if ret != 0:
        raise Exception("add svn Error!:"+path)
    else:
        print("add ok!")
    os.chdir(cur_path)


def add_svn_force(path):
    command = f'''svn add {path} --force '''
    ret = os.system(command)
    print(command)
    if ret != 0:
        raise Exception("add force Error!:"+path)
    else:
        print("add ok!")
