#coding=utf-8
# save the match into the file
# Author:ZJW
import csv
import csvdata

def savedata(data):
    csvfile = file(u'F:\\研究生之\\20171127\\output.csv','wb')
    writer = csv.writer(csvfile)
    writer.writerow(['rknum','cknum','rkcph','ckcph'])
    writer.writerows(data)
    csvfile.close()

def opencph_in(zzs):  # list  zzs车轴为5
	cph_in = list()  # 入站数据的车牌号列表
	with open(u'F:\\研究生之\\20171127\\_2015_6_2015_6_7_in.csv','rb') as csvfile:#打开一个文件
		reader = csv.DictReader(csvfile)#返回以字典为元素的数组
		column = [row for row in reader]
	
	for row in column:  # 逐行获取每一个Dict字典
		if row['zzs'] == zzs:
			cph_in.append(row['cph'])  # cph_in
	return cph_in
	
def opencph_out(zzs):  # list  zzs车轴为5
	cph_out = list()  # 出站数据的车牌号列表
	with open(u'F:\\研究生之\\20171127\\_2015_6_2015_6_7_out.csv','rb') as csvfile:#打开一个文件
		reader = csv.DictReader(csvfile)  # 返回以字典为元素的数组
		column = [row for row in reader]
	
	for row in column:  # 逐行获取每一个Dict字典
		if row['zzs'] == zzs:
			cph_out.append(row['cph'])  # cph_out
	return cph_out
	
if __name__ == '__main__':
    data = [(1,2,1,2),(2,3,4,5)]
    # savedata(data)
    cph_in = opencph_in('6')
    cph_out = opencph_out('6')
    for i in cph_out:
       print i.decode('utf-8') 
    # print cph_in,type(cph_in)
    # print cph_out,type(cph_out)