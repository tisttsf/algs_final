type_of_gold=['reliable','unreliable']
first_blood_time=150
sum_of_procession=0
gold_assit_range=1300
comeback_relation=[0,1]
assit_hero_num=[0,1,2,3,4,5]
dead_hero_level=range(1,25)
poor_relation=[1,2,3,4,5]
# rank_relation=[1,2,3,4,5,6,7,8,9,10]
base_num=[1,2,4,5.6,7.0]
pro_rank=[[1],[1.3,0.7],[1.3,1,0.7],[1.3,1.1,0.9,0.7],[1.3,1.15,1,0.85,0.7]]
def get_kill_money(num_of_assit_hero,rank_me,rank_dead,comback,dead_procession,level_of_dead,state):
	assert num_of_assit_hero>=rank_me
	assert num_of_assit_hero>=0
	assert rank_dead>=0
	assert rank_me>=0
	assert level_of_dead>=1 and level_of_dead<=25

	poor_coe=1.2-0.15*rank_dead
	pro_coe=pro_rank[num_of_assit_hero][rank_me]
	ut=(126/base_num[num_of_assit_hero])+(4.5-0.9*num_of_assit_hero)*level_of_dead+comback*(dead_procession*0.026+70)/(num_of_assit_hero+1)
	utt=pro_coe*poor_coe*ut
	print (poor_coe)
	print (pro_coe)
	return utt

# lostmoney=50+pro/40
# buyback=100 +pro/13
# buyback_cooldown=8*60
# buyback_punishment=[0,25]
# reborn_time=4*level+buyback_punishment[0]



print (get_kill_money(1,0,0,1,600,1,0))