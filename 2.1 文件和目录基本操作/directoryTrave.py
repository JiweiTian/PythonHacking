# -*- coding: UTF-8 -*-
import sys
import os


os.chdir('K:/Software/Microsoft VS Code/PythonHacking/2.1 文件和目录基本操作/sampleDirectory')

def listCurrentDirectory(path):
    files = os.listdir(path)
    for name in files:
        print(name)

listCurrentDirectory('.')

def listDirectoryDetail(path):
        files = os.listdir(path)
        for name in files:
                pathName = os.path.join(path, name)
                print(os.stat(pathName).st_mode)
                print(os.stat(pathName).st_ino)
                print(os.stat(pathName).st_dev)
                print(os.stat(pathName).st_nlink)
                print(os.stat(pathName).st_uid)
                print(os.stat(pathName).st_gid)
                print(os.stat(pathName).st_size)
                print(os.stat(pathName).st_atime)
                print(os.stat(pathName).st_mtime)
                print(os.stat(pathName).st_ctime)

listDirectoryDetail('.')

import stat
def listCurrentDirectoryMode(path):
        files = os.listdir(path)
        for name in files:
                pathName = os.path.join(path, name)
                mode = os.stat(pathName).st_mode
                if stat.S_ISDIR(mode):
                        print('%s是文件夹' % pathName)
                elif stat.S_ISREG(mode):
                        print('%s是文件' % pathName)
                else:
                        print('未知目录类型 %s' % pathName)
listCurrentDirectoryMode('.')

def printChmode(path):
        files = os.listdir(path)
        for name in files:
                pathName = os.path.join(path, name)
                mode = os.stat(pathName).st_mode
                print(stat.filemode(mode))

printChmode('.')


def walkDir(path):
        for dirName, subdirList, fileList in os.walk(path):
                print('发现目录：%s' % dirName)
                for fname in fileList:
                        print('\t%s' % fname)

walkDir('.')

os.chmod("./b.txt",stat.S_IXGRP)

os.chmod("./b.txt",stat.S_IWOTH)

def renameTest():
        walkDir('.')
        os.rename('b.txt','vvvv.txt')
        try:
                os.rename('./ccc/nnnn.txt', './ccc/mmmm.txt')
        except FileNotFoundError as e:
                print(e)
        os.renames('./aaa/bbbbbb/bbbb.txt','./aaa/bbbbbb/new.txt')
        walkDir('.')

#renameTest()

def createPath(p):
        try:
                os.makedirs(p)
        except OSError as e:
                print('创建目录失败',e)
        else:
                print('创建%s成果' % p)

createPath('./a/') 

def createPath2(p):
        try:
                if not os.path.exists(p):
                        os.makedirs(p)
                        print('%s创建成功' % p)
                else:
                        print('%s已经存在' % p)
        except OSError as e:
                print('创建目录失败',e)
createPath2('./a/')
createPath2('./a/c/')


def createPath3(p,mode):
        try:
                if not os.path.exists(p):
                        os.makedirs(p,mode)
                        print('%s创建成功' % p)
                        mode = os.stat(p).st_mode
                        print(stat.filemode(mode))
                else:
                        print("%s已经存在" % p)
        except OSError as e:
                print('创建目录失败',e)
        
createPath3('./a/b/c',0o755)


import tempfile
def createTempDirectory():
        with tempfile.TemporaryDirectory() as directory:
                print('临时目录 %s' % directory)

createTempDirectory()

def removeDir(path):
        try:
                os.rmdir(path)
        except OSError:
                print('删除 %s 失败' % path)
        else:
                print('删除 %s 成功' % path)

removeDir('./a/b/c/')

print('作业')
def listCurrentDirectoryall(path):
        files = os.listdir(path)
        for name in files:
                pathName = os.path.join(path, name)
                mode = os.stat(pathName).st_mode
                print('%s' % name)
                if stat.S_ISDIR(mode):
                        print('%s是文件夹' % pathName)
                        listCurrentDirectoryall(pathName)
                elif stat.S_ISREG(mode):
                        print('%s是文件' % pathName)
                else:
                        print('未知目录类型 %s' % pathName)
listCurrentDirectoryall('.')