# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# sdf.py
# Created on: 2016-02-15
# Author by: guyanf@163.com
# Description: mesh中poi数据的合并处理
# ---------------------------------------------------------------------------


import sys
import os
import arcpy

def do_POIMerge(sourceDir):

    i = 0 # 计数，裁切框数

    # 设置工作空间位置
    # arcpy.env.workspace = sourceDir

    for root, dirnames, files in os.walk(sourceDir) :
        r, parentName = os.path.split(root)

        arcpy.env.workspace = sourceDir

        arcpy.Merge_management(files, os.path.join(sourceDir, 'ok.dbf'))


if __name__ == '__main__':
    print 'start'
    sourceDir = u"E:\\new\\data\\ing\\poi" # 原始文件存放路径
    do_POIMerge(sourceDir)
    print "all is ok"
