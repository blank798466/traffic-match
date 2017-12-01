# coding=utf-8
# get the diffdata and the index from the list
# Input:time_in,time_out,height_in,height_out
# Output:difftime_in,difftime_out,diffheight_in,diffheight_out,index_in,index_out
# Author:ZJW
import time
import datetime
import csvdata
import evlfunc
import connectingcar
RATIO = 0.2

# 转换datetime
def changetime(time1,time2):
    time_in = list()  # 入站时间datetime类型列表
    time_out = list()  # 出站时间datetime类型列表
    # 将时间类型进行转化，string-time-datetime
    for ti1 in time1:
        t1 = time.strptime(ti1,"%Y-%m-%d %H:%M:%S")  # 字符串string类型时间转换成time类型时间
        t11 = datetime.datetime(t1[0],t1[1],t1[2],t1[3],t1[4],t1[5])  # time类型时间转换成datetime类型时间
        time_in.append(t11)

    for ti2 in time2:
        t2 = time.strptime(ti2,"%Y-%m-%d %H:%M:%S")  # 字符串string类型时间转换成time类型时间
        t22 = datetime.datetime(t2[0],t2[1],t2[2],t2[3],t2[4],t2[5])  # time类型时间转换成datetime类型时间
        time_out.append(t22)
    return time_in,time_out

# 计算出入站数据时间差列表以及对应的index
def caltime(time_in,time_out):
    difftime_in = [[] for n in range(len(time_in))]  # 入站单个数据对应其他出站车辆数据的时间差列表
    difftime_out = [[] for n in range(len(time_out))]  # 入站单个数据对应其他入站车辆数据的时间差列表
    index_in = [[] for n in range(len(time_in))]  # 记录时间差列表的入站的每一条数据对应出站车辆数据的index
    index_out = [[] for n in range(len(time_out))]  # 记录时间差列表的出站的每一条数据对应入站车辆数据的index

    for i in range(len(time_in)):  # 出站
		for j in range(len(time_out)):  # 入站
            # 比较时间datetime类型大小加以减法运算,入站时间一定大于出站时间
			diff_in_seconds = (time_in[i] - time_out[j]).seconds
			diff_in_days = (time_in[i] - time_out[j]).days
			diff_in = diff_in_days * 86400 + diff_in_seconds
			if diff_in in range(400,4000):  # 时间差范围设置为（400s,4000s）
				index_in[i].append(j)
				difftime_in[i].append(diff_in)
    for x in range(len(time_out)):  # 出站
		for y in range(len(time_in)):  # 入站
            # 比较时间datetime类型大小加以减法运算,入站时间一定大于出站时间
			diff_out_seconds = (time_in[y] - time_out[x]).seconds
			diff_out_days = (time_in[y] - time_out[x]).days
			diff_out = diff_out_days * 86400 + diff_out_seconds
			if diff_out in range(400,4000):  # 时间差范围设置为（400s,4000s）
				index_out[x].append(y)
				difftime_out[x].append(diff_out)
    return difftime_in,difftime_out,index_in,index_out

# 计算入站数据重量差列表并更新时间差列表和index
def calheight_in(height1,height2,time_in,index1):
    diffheight_in = [[] for n in range(len(height1))]  # 入站单个数据对应其他出站车辆数据的车重差列表
    difftime_in = [[] for n in range(len(time_in))]  # 用于更新
    index_in = [[] for n in range(len(index1))]
    diff = None
    
    for i in range(len(height1)):  # 入站
        for j in range(len(height2)):  # 出站
            if j in index1[i]:
                diff = abs(int(height1[i]) - int(height2[j]))
                if diff < int(height2[j]) * RATIO:
                    diffheight_in[i].append(diff)
                    # print index1[i],i,j
                    # print '---'
                    difftime_in[i].append(time_in[i][index1[i].index(j)])
                    index_in[i].append(j)
                    
    return diffheight_in,difftime_in,index_in
    
# 计算出站数据重量差列表并更新时间差列表和index
def calheight_out(height1,height2,time_out,index2):
    diffheight_out = [[] for n in range(len(height2))]  # 入站单个数据对应其他出站车辆数据的车重差列表
    difftime_out = [[] for n in range(len(time_out))]  # 用于更新
    index_out = [[] for n in range(len(index2))]
    diff = None
    
    for i in range(len(height2)):  # 出站
        for j in range(len(height1)):  # 入站
            if j in index2[i]:
                diff = abs(int(height2[i]) - int(height1[j]))
                if diff < int(height2[i]) * RATIO:
                    diffheight_out[i].append(diff)
                    # print index1[i],i,j
                    # print '---'
                    difftime_out[i].append(time_out[i][index2[i].index(j)])
                    index_out[i].append(j)
                    
    return diffheight_out,difftime_out,index_out
    
'''
# 计算出入站数据重量差列表，仅按照时间差列表进行选择
def calheight(height1,height2,index_in,index_out):
    diffheight_in = [[] for n in range(len(height1))]  # 入站单个数据对应其他出站车辆数据的车重差列表
    diffheight_out = [[] for n in range(len(height2))]  # 出站单个数据对应其他入站车辆数据的车重差列表
    for i in range(len(index_in)):
		for j in range(len(index_out)):
			if j in index_in[i]:
				diffheight_in[i].append(abs(int(height1[i]) - int(height2[j])))
    for x in range(len(index_out)):
		for y in range(len(index_in)):
			if y in index_out[x]:
				diffheight_out[x].append(abs(int(height2[x]) - int(height1[y])))
    return diffheight_in,diffheight_out	
'''   
if __name__ == '__main__':
    # time1,time2 = opencsv_out('5')  # zzs车轴为5
    time1 = csvdata.opencsv_in('5')[0]
    time2 = csvdata.opencsv_out('5')[0]
    height1 = csvdata.opencsv_in('5')[1]
    height2 = csvdata.opencsv_out('5')[1]
    time_in = changetime(time1, time2)[0]
    time_out = changetime(time1, time2)[1]
    difftime_in = caltime(time_in, time_out)[0]
    difftime_out = caltime(time_in, time_out)[1]
    index_in = caltime(time_in, time_out)[2]
    index_out = caltime(time_in, time_out)[3]
    # print len(time1)
    # print len(time2)
    # print height1
    # print height2
    
    '''
    print difftime_in
    print difftime_out
    print index_in
    print index_out
    
    diffheight_in = calheight(height1, height2,index_in,index_out)[0]
    diffheight_out = calheight(height1, height2,index_in,index_out)[1]
    # h_index_in = calheight(height1, height2)[2]
    # h_index_out = calheight(height1, height2)[3]
    print diffheight_in
    print diffheight_out
    # print h_index_in
    # print h_index_out
    rkdata = evlfunc.getdata(difftime_in,diffheight_in)
    ckdata = evlfunc.getdata(difftime_out,diffheight_out)
    print rkdata
    print ckdata
    rkpri = evlfunc.getpri(rkdata, index_in)
    ckpri = evlfunc.getpri(ckdata, index_out)
    print rkpri
    print ckpri
    connectingcar.find_stable_matching(rkpri,ckpri)

    diffheight_in = calheight(height1,height2,difftime_in,difftime_out,index_in,index_out)[0]
    diffheight_out = calheight(height1,height2,difftime_in,difftime_out,index_in,index_out)[1]
    difftime_in = calheight(height1,height2,difftime_in,difftime_out,index_in,index_out)[2]
    difftime_out = calheight(height1,height2,difftime_in,difftime_out,index_in,index_out)[3]
    index_in = calheight(height1,height2,difftime_in,difftime_out,index_in,index_out)[4]
    index_out = calheight(height1,height2,difftime_in,difftime_out,index_in,index_out)[5]
    print diffheight_in
    print diffheight_out
    print difftime_in
    print difftime_out
    print index_in
    print index_out'''
    print calheight_in(height1,height2,difftime_in,index_in)[0]
    print calheight_in(height1,height2,difftime_in,index_in)[1]
    print calheight_in(height1,height2,difftime_in,index_in)[2]
    print calheight_out(height1,height2,difftime_out,index_out)[0]
    print calheight_out(height1,height2,difftime_out,index_out)[1]
    print calheight_out(height1,height2,difftime_out,index_out)[2]