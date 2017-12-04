#coding=utf-8
# get the data from .csv to the list
# Input:_2015_6_2015_6_7_in.csv,_2015_6_2015_6_7_out.csv
# Output:time_in,time_out,height_in,height_out
# Author:ZJW
import csv
def opencsv_in(zzs):  # list  zzs车轴为5
	time_in = list()  # 入站数据的时间列表
	height_in = list()  # 入站数据的车重列表
	with open(u'F:\\研究生之\\20171127\\_2015_6_2015_6_7_in.csv','rb') as csvfile:#打开一个文件
		reader = csv.DictReader(csvfile)#返回以字典为元素的数组
		column = [row for row in reader]
	
	for row in column:  # 逐行获取每一个Dict字典
		if row['zzs'] == zzs:
			time_in.append(row['rksj'])  # rksj_in
			height_in.append(row['chzz'])  # chzz_in
	return time_in,height_in
	
def opencsv_out(zzs):  # list  zzs车轴为5
	time_out = list()  # 出站数据的时间列表
	height_out = list()  # 出站数据的车重列表
	with open(u'F:\\研究生之\\20171127\\_2015_6_2015_6_7_out.csv','rb') as csvfile:#打开一个文件
		reader = csv.DictReader(csvfile)#返回以字典为元素的数组
		column = [row for row in reader]
	
	for row in column:  # 逐行获取每一个Dict字典
		if row['zzs'] == zzs:
			time_out.append(row['cksj'])  # rksj_in
			height_out.append(row['chzz'])  # chzz_in
	return time_out,height_out
    
if __name__ == '__main__':
    time1 = opencsv_in('5')[0]
    time2 = opencsv_out('5')[0]
    height1 = opencsv_in('5')[1]
    height2 = opencsv_out('5')[1]
    print time1
    print time2
    print height1
    print height2