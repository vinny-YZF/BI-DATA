#数据可视化
import matplotlib.pyplot as plt

x = [28, 29, 30]
y1 = [0.2722,0.2726,0.2286]
y2 = [0.2734, 0.273,0.2857]
y3 = [0.2726, 0.2727,0.3]
y4 = [0.1819, 0.1817,0.1857]

plt.title('level')  
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.xlabel('time')  # 
plt.ylabel('percentage')  # 
plt.plot(x, y1, marker='o', markersize=3)  # 
plt.plot(x, y2, marker='o', markersize=3)
plt.plot(x, y3, marker='o', markersize=3)
plt.plot(x, y4, marker='o', markersize=3)


for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y4):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)


plt.legend(['leve10', 'level20', 'level30','level40'])  

plt.show()  


x = [28, 29, 30]
y1 = [0.3335,0.3333,0.3143]
y2 = [0.3329, 0.3333,0.3571]
y3 = [0.3336, 0.3334,0.3286]


plt.title('channel') 
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.xlabel('time') 
plt.ylabel('percentage')  
plt.plot(x, y1, marker='o', markersize=3)  
plt.plot(x, y2, marker='o', markersize=3)
plt.plot(x, y3, marker='o', markersize=3)



for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)



plt.legend(['APP', 'wap', 'web']) 

plt.show()  


x = [28, 29, 30]
y1 = [0.3068,0.2969,0.3857]
y2 = [0.3373, 0.3267,0.3]
y3 = [0.3064, 0.3267,0.2857]


plt.title('web')  
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.xlabel('time')  #
plt.ylabel('percentage')  
plt.plot(x, y1, marker='o', markersize=3)  
plt.plot(x, y2, marker='o', markersize=3)
plt.plot(x, y3, marker='o', markersize=3)



for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y3):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)



plt.legend(['forum', 'main', 'main（www)'])  

plt.show() 
