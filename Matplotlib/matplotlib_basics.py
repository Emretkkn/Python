import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
'''
x = [1,2,3,4]
y = [1,4,9,16]
# plt.plot(x,y,"--")
plt.plot(x,y,"o:b")
plt.axis([0,6,0,20])
plt.title("Grafik Başlığı")
plt.xlabel("X etiketi")
plt.ylabel("Y etiketi")
plt.show()
'''
'''
x = np.linspace(0,2,100)
plt.plot(x,x,label="Linear",color="red")
plt.plot(x,x**2,label="Quadratic",color="green")
plt.plot(x,x**3,label="Cubic",color="blue")
plt.plot(x,np.log(x),label="Log",color="magenta")
plt.xlabel("X etiketi")
plt.ylabel("Y etiketi")
plt.legend()
plt.title("Sample Plot")
plt.show()
'''
'''
x = np.linspace(0,2,100)
fig,axs = plt.subplots(4)
axs[0].plot(x,x,color="green")
axs[0].set_title("linear")
axs[1].plot(x,x**2,color="red")
axs[1].set_title("quadratic")
axs[2].plot(x,x**3,color="cyan")
axs[2].set_title("cubic")
axs[3].plot(x,x**4,color="purple")
plt.tight_layout()
plt.show()
'''
'''
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("Figure Title")
axs[0,0].plot(x,x,color="green")
axs[0,0].set_title("linear")
axs[0,1].plot(x,x**2,color="red")
axs[0,1].set_title("quadratic")
axs[1,0].plot(x,x**3,color="cyan")
axs[1,0].set_title("cubic")
axs[1,1].plot(x,np.log(x),color="brown")
axs[1,1].set_title("Logic")
plt.tight_layout()
plt.show()
'''
df = pd.read_csv("nba/all_seasons.csv")
choosen = df[["player_name","team_abbreviation","country","age","pts","reb","ast"]].groupby("team_abbreviation").mean(numeric_only=True)
choosen.plot(subplots=True)
plt.legend()
plt.show()

