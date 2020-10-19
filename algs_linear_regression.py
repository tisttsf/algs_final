import matplotlib.pyplot as plt
import numpy as np

#load data from file
#从txt文件导入数据，
# X=np.hstack()
# W=np.zeros((2,1))
def load_data(filename):
    data = []
    file = open(filename)
    for line in file.readlines():#readlines注意了
        lineArr = line.strip().split(',')
        col_num = len(lineArr)
        temp = []
        for i in range(col_num):
            temp.append(float(lineArr[i]))
        data.append(temp)
    return np.array(data)

#打印出来看一下数据集大小  
data = load_data('ex1data1.txt')
print (data.shape)
# print (data[:5])

X = data[:,:-1]
y = data[:,-1:]
print (X.shape)
print (y.shape)
#print (X[:5])
#print (y[:5])
# plt.scatter(X,y,color = 'r',marker= 'x')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.show()



# #compute the cost 
num_train = X.shape[0]
one = np.ones((num_train,1)) 
print (one,type(one))
X = np.hstack((one,data[:,:-1])) #add ones
W = np.zeros((2,1)) #w0 ,w1
print (X.shape)
# print (W)
# #定义一下计算cost的函数，并且测试一下是否正确
def compute_cost(X_test,y_test,theta):
    num_X = X_test.shape[0]
    cost = 0.5 * np.sum(np.square(X_test.dot(theta) - y_test)) / num_X
    return cost
d=np.array([1.0,2,3])
print (d,d.shape)
print (d.dot([1,2]))

cost_1 = compute_cost(X,y,W)
print ('cost =%f,with W =[0,0]'%(cost_1))
print ('Expected cost value (approx) 32.07')
cost_2 = compute_cost(X,y,np.array([[-1],[2]]))
print ('cost =%f,with W =[-1,2]'%(cost_2))
print ('Expected cost value (approx) 54.24')