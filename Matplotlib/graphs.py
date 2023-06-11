import matplotlib.pyplot as plt
import numpy as np
'''
# Stack Plot
years=[2011,2012,2013,2014,2015]
player1=[8,12,15,21,26]
player2=[17,11,8,9,15]
player3=[30,28,25,34,40]

plt.plot([],[],color="r",label="Player1")
plt.plot([],[],color="g",label="Player2")
plt.plot([],[],color="b",label="Player3")
plt.stackplot(years,player1,player2,player3,colors=["r","g","b"])
plt.title("Players goals per year")
plt.xlabel("Years")
plt.ylabel("Goals")
plt.legend()
plt.show()
'''
'''
# Pie chart
goal_types = "Penaltı","Kaleye Atılan Şut","Serbest Vuruş"
goals = [20,56,8]
colors = ["r","g","b"]
plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct='%1.1f%%')
plt.show()
'''
'''
# Bar Chart
plt.bar([0.25,0.50,0.75,1.75,4.45,5.42,3.21],[10,30,20,40,50,15,60],label="BMW",width=.5)
plt.bar([1.25,2.50,4.75,3.75,6.45,2.85,5.56],[16,54,28,33,62,18,70],label="Audi",width=.5)
plt.xlabel("Gün")
plt.ylabel("Gidilen Mesafe (km)")
plt.title("Araç Bilgileri")
plt.legend()
plt.show()
'''
'''
# Histogram
yaslar = np.random.randint(10,100,50)
yas_gruplari = [10,20,30,40,50,60,70,80,80,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.6)
plt.xlabel("Yaşlar")
plt.ylabel("Yaş Grupları")
plt.title("Histogram Grafiği")
plt.show()
'''