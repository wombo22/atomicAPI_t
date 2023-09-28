import os, time

def clean_file_open(filepath, readOrWrite, writingContent=None, extraWarn=None, truncate=None):
    if type(readOrWrite) != str:
        print("for argument 2 'readOrWrite' enter r or w as a STRING")
    if extraWarn != None:
        if type(extraWarn) != str:
            print("for OPTIONAL argument 4 `extraWarn` enter your warning as a STRING")
    else:
        extraWarn  = ""
    if readOrWrite == "w":
        if writingContent == None:
            print("you must provide writingContent argument if using w as 2nd argument")
        else:
            try:
                f = open(filepath, "w")
                f.write(str(writingContent))
                if truncate == True:
                    f.truncate()
                f.close()
            except:
                return "cant write " + writingContent + "to:" + filepath + "\n" +  extraWarn
    elif readOrWrite == "r":
        if os.path.isfile(filepath) == True:
            f = open(filepath, "r")
            content = f.read()
            f.close()
            return content
        else:
            err = filepath + " cannot be found!\n " +  extraWarn
    else:
        print("unknown argument", readOrWrite , "\nfor argument 2 'readOrWrite' enter r or w as a string")
        
def wait_for_file(path, tries=None):
    if tries == None:
        while True:
            if os.path.isfile(path):
                return
            else:
                time.sleep(1)
                continue
    else:
        if type(tries) != type(int):
            print("tries must be an int type")
        i = 0
        while i < tries:
            if os.path.isfile(path):
                return
            else:
                time.sleep(1)
                i = i + 1
                continue

def clean_mkdir(dirpath):
    if os.path.isdir(dirpath) == True:
#        print("dir already exists!")
        return False
    else:
        os.mkdir(dirpath)
        return True

def clearDirPath(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

   
def copy(target, dest):
    command = "cp " + target + " " + dest
    os.popen(command).read()

def switchdirpath(fullpath, destdir):
    #changes full dir/path to destdir/path #WILL ONLY CHANGE THE VERY FIRST DIR IF MULTIPLE ARE GIVEN
    if fullpath.find("/") == -1:
        print("fullpath does not contain \'/\' , wont modify")
        return False
    else:
        fullpath_splitlist = fullpath.split("/")
        fullpath_splitlist[0] = destdir
        separator = "/"
        newpath = separator.join(fullpath_splitlist)
        return newpath

