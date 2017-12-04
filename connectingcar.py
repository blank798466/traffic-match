#coding=utf-8
# Implementing the Gale-Shaoley algorithm
# Input:rkMP,ckWP
# Output:match
# Author:ZJW
'''
while  存在男人m是自由的且还没对每个女人都求过婚
      选择这个男人m
                令w是m的优先表中还没求过婚的最高排名的女人
        if  w是自由的  
            （m，w）变成约会状态
        else  w当前与m1约会
              if  w更偏爱m1而不爱m
                    m保持自由
              else    w更偏爱m而不爱m1
                   （m，w）变成约会状态
                    m1变成自由
              endif
                  endif
endwhile
'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def find_stable_matching(rkMP, ckWP):
	'''
	定义两个列表MP和WP，男人和女人数目范围为[0, n-1]
	MP，WP是二维数组，分别存储着男人女人各自对异性的偏爱程度排序
	输出一组包含着男女匹配的数组数据（i，j）
	'''
	m = len(rkMP)  # 入站车辆的个数
	n = len(ckWP)  # 出站车辆的个数
	# 出入口个数不同导致循环判断无法结束
	isRkFree = [True] * m  # 入站车辆是否全部自由，也就是未匹配
	isCkFree = [True] * n  # 出站车辆是否全部自由，也就是未匹配
	isRkProposed = [[False for i in range(n)] for j in range(m)]  # 定义二维数组，入站是否与出站匹配
	match = []  # 定义出入口匹配数组
	'''sum = 0  # 匹配次数
	sum1 = 0  # 应匹配次数
	for i in range(len(rkMP)):
		sum1 += len(rkMP[i])'''
	
	while(True in isRkFree):  # 存在入站是自由的
		indexR = isRkFree.index(True)  # 获取自由的入口车辆的序号
		indexC = None  # 初始化出站车辆的序号
		for i in range(len(rkMP[indexR])):  
			w = rkMP[indexR][i]  # w是m的优先表中的出站车辆
			if(not isRkProposed[indexR][w]):  # w还没有匹配且最高排名                                                                
				indexC = w
				break 
		if indexC is not None:  
			isRkProposed[indexR][indexC] = True  # 这个入站车辆和w出站匹配状态改为TRUE
			# sum += 1
			if(isCkFree[indexC]):  # w是否自由
				isCkFree[indexC] = False  # 出站车辆状态改为不自由
				isRkFree[indexR] = False  # 入站车辆状态改为不自由
				match.append((indexR, indexC))  # m,w变为匹配状态
			else: # w已经不自由
				indexM1 = -1  # 初始化w目前匹配状态的入站车辆
				for j in range(len(match)):
					if(match[j][1] == indexC):  # 找出w目前匹配状态的入站车辆的序号
						indexM1 = match[j][0]    
						break
				if(indexR not in ckWP[indexC]):
					continue
				if(indexM1 not in ckWP[indexC])and(indexR in ckWP[indexC]):  # 如果w根本不爱m1
					isRkFree[indexM1] = True  # m1变成自由
					isRkFree[indexR] = False  # m变为不自由
					for k in range(len(match)):  # 解除原有m1匹配状态
						if(match[k][1] == indexC):  # 找出w目前匹配状态的入站车辆的序号
							del match[k]
							break
					match.append((indexR, indexC))  # m,w变为匹配状态	
				if((indexM1 in ckWP[indexC])and(indexR in ckWP[indexC])):  
					if(ckWP[indexC].index(indexR) < ckWP[indexC].index(indexM1)):# 比较w更偏爱m还是m1，如果w更偏爱m
						isRkFree[indexM1] = True  # m1变成自由
						isRkFree[indexR] = False  # m变为不自由
						for k in range(len(match)):
							if(match[k][1] == indexC):  # 找出w目前匹配状态的入站车辆的序号
								del match[k]
								break
						match.append((indexR, indexC))  # m,w变为匹配状态
		else:  # 入口数据与所有优先级内的元素数据全部匹配过还显示自由状态
			isRkFree[indexR] = False
	return match
	
def test4():
	MP = [[2,1],[2],[1],[1,0]]
	WP = [[1,0],[2,0],[2,3,1]]
	SM = find_stable_matching(MP,WP)
	
if __name__ == "__main__":
	print "**********test4************"
	test4()