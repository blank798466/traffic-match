#coding=utf-8
# make two double dimensional arrays into the priority order by the evaluation function
# Input:dirmatch,time_in,time_out,height_in,height_out
# Output:rkMP,ckWP
# Author:ZJW
'''
评价函数F = k1 * (time - mean_time)/var_time + k2 * height/var_height
将四个二维数组difftime_in,difftime_out,diffheight_in,diffheight_out
转换成两个出入站的评价函数大小的二维数组rkdataMP,ckdataWP
然后转换成两个出入站的优先级顺序的二维数组rkMP,ckWP
'''
k1 = 0.5 
k2 = 0.5
mean_time = 1190.49
mean_height = 631.73
var_time = 700.935
var_height = 788.905

# 车辆数据的评价函数的二维数组kdata
def getdata(difftime,diffheight):  
    kdata = [[] for i in range(len(difftime))]
    for i in range(len(difftime)):
        for j in range(len(difftime[i])):
            if difftime[i] and diffheight[i]:
                t1 = difftime[i][j]
                h2 = diffheight[i][j]
                fk = k1 * (t1 - mean_time) / var_time + k2 * h2 / var_height
                kdata[i].append(fk)
    return kdata
    
# 车辆数据优先级顺序的二维数组pri
def getpri(kdata, kindex):
	len_k = len(kdata)
	pri = [[] for i in range(len_k)]
	for i in range(len_k):
		sorted_k = sorted(kdata[i])
		for j in sorted_k:
			num = kdata[i].index(j)
			pri[i].append(kindex[i][num])
	return pri

if __name__ == '__main__':
    a=[[],[644],[1234,343]]
    b=[[],[66],[5534,3423]]
    e=[[],[0],[1,2]]
    c=getdata(a,b)
    d=getpri(c,e)
    print c
    print d