import random
"给定一串(具有负数意义的)数字,找出其中和为最大值的片段,并给出下标和结果."
sequence=list()
for i in range(5):
	sequence.append(random.randint(-10,10))
#sequence=[7,5]
start,end=0,len(sequence)
def max_seq_value(start,end,max_or_min=1):
	if len(sequence)==0:
		return
	if len(sequence)==1:
		return (0,0,sequence[0])
	if abs(start-end)==1:
		t=(start,end-1,sum(sequence[start:end]))
		return t
	else:
		mid=(start+end)//2	
		start_left,end_left,max_left=max_seq_value(start,mid)
		start_right,end_right,max_right=max_seq_value(mid,end)
		mid_value,target_left,target_right=mid_max(start,mid,end)
		m=max([max_left,max_right,mid_value])
		if m==max_left:
			return (start_left,end_left,max_left)
		elif m==max_right:
			return (start_right,end_right,max_right)
		else:
			return (target_left,target_right,mid_value)

def mid_max(start,mid,end):
	max_left,max_right=float("-inf"),float("-inf")
	max_tmp_left,max_tmp_right=0,0
	tmp_left_index,tmp_right_index=0,0
	for i in range(mid-1,start,-1):
		max_tmp_left+=sequence[i]
		if max_tmp_left>max_left:
			max_left=max_tmp_left
			tmp_left_index=i
	for j in range(mid,end):
		max_tmp_right+=sequence[j]
		if max_tmp_right>max_right:
			max_right=max_tmp_right
			tmp_right_index=j
	return max_left+max_right,tmp_left_index,tmp_right_index
"复杂度手动分析"


"简单测试,一串只有正负意义的数字,求出它们之中的最大子和或最小子和"
if __name__ == '__main__':
	print (sequence)
	c=max_seq_value(0,end)
	print (c)
""


"实际应用:股票收益,日增长率"