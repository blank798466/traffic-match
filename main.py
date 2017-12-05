# coding=utf-8
# Input:_2015_6_2015_6_7_in.csv,_2015_6_2015_6_7_out.csv
# Output:match
# Author:ZJW
import csvdata
import diffdata
import evlfunc
import connectingcar
import storage
import time
import codecs

'''
2轴车：1min26s   200duo
3轴车: 23s   100duo
4轴车：22s
5轴车: 2s
6轴车: 6min57    500duo
设置定时器进行验证
'''

def run(zss,k1,k2):
	time1 = csvdata.opencsv_in(zss)[0]
	time2 = csvdata.opencsv_out(zss)[0]
	height1 = csvdata.opencsv_in(zss)[1]
	height2 = csvdata.opencsv_out(zss)[1]
	# print time1  # 入站时间数组，string类型
	# print time2  # 出战时间数组，string类型
	# print height1  # 入站车重数组
	# print height2  # 出站车重数组

	time_in = diffdata.changetime(time1, time2)[0]
	time_out = diffdata.changetime(time1, time2)[1]
	# print time_in  # 入站时间数组，datetime类型
	# print time_out  # 出站时间数组，datetime类型

	difftime1 = diffdata.caltime(time_in, time_out)[0]
	difftime2 = diffdata.caltime(time_in, time_out)[1]
	index1 = diffdata.caltime(time_in, time_out)[2]
	index2 = diffdata.caltime(time_in, time_out)[3]
	# print difftime1  # 符合时间差条件下的入站时间差数组
	# print difftime2  # 符合时间差条件下的出站时间差数组
	# print index1  # 符合时间差条件下的入站序列数组
	# print index2  # 符合时间差条件下的出站序列数组

	diffheight_in = diffdata.calheight_in(height1,height2,difftime1,index1)[0]
	diffheight_out = diffdata.calheight_out(height1,height2,difftime2,index2)[0]
	difftime_in = diffdata.calheight_in(height1,height2,difftime1,index1)[1]
	difftime_out = diffdata.calheight_out(height1,height2,difftime2,index2)[1]
	index_in = diffdata.calheight_in(height1,height2,difftime1,index1)[2]
	index_out = diffdata.calheight_out(height1,height2,difftime2,index2)[2]
	# print diffheight_in  # 符合重量差和时间差条件的入站重量差数组
	# print diffheight_out  # 符合重量差和时间差条件的出站重量差数组
	# print difftime_in  # 符合重量差和时间差条件的入站时间差数组
	# print difftime_out  # 符合重量差和时间差条件的出站时间差数组
	# print index_in  # 符合重量差和时间差条件的入站序列数组
	# print index_out  # 符合重量差和时间差条件的出站序列数组

	rkdata = evlfunc.getdata(difftime_in,diffheight_in,k1,k2)
	ckdata = evlfunc.getdata(difftime_out,diffheight_out,k1,k2)
	# print rkdata  # 入口车辆数据的评价函数
	# print ckdata  # 出口车辆数据的评价函数

	rkpri = evlfunc.getpri(rkdata,index_in)
	ckpri = evlfunc.getpri(ckdata,index_out)
	# print rkpri  # 入口车辆数据优先级顺序数组
	# print ckpri  # 出口车辆数据优先级顺序数组

	match = connectingcar.find_stable_matching(rkpri,ckpri)
	# print match  # 匹配结对的数据

	cph_in = storage.opencph_in(zss)
	cph_out = storage.opencph_out(zss)
	t = 0
	f = 0
	for i in match:
		#print cph_in[i[0]].decode('utf-8'),'---',cph_out[i[1]].decode('utf-8')
		if cph_in[i[0]] == cph_out[i[1]]:
			t += 1
		else:
			f += 1
	print t / float(t + f)
	storage.savedata(match,cph_in,cph_out)  # 将match存储进.csv中

if __name__ == "__main__":
	time_start=time.time();#time.time()为1970.1.1到当前时间的毫秒数
	zss = '2'
	k1 = 0.5
	k2 = 0.5
	'''
	for i in range(100):
		for j in range(100 - i):
			run(zss,float(i)/100,float(j)/100)
			'''
	run(zss,k1,k2)
	time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
	t = time_end - time_start
	wr = zss + u"轴车的运行时间为:" + str(t) + 's'
	#print wr
	# print type(wr)
	'''
	with codecs.open(u'F:\\研究生之\\20171127\\time.txt','a','utf-8') as f:
		f.write('\n'+wr)
	'''
