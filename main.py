import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import firstsensor
import datetime as dt
import time


fig = plt.figure(figsize=(10,6))
axes = fig.add_subplot(1, 1, 1)
plt.xticks(rotation=45, ha='right')
y1 = np.array([dt.time(i, 0) for i in range(0, 23)])
t = range(len(y1))
x, y = [], []
x2, y2 = [], []

try:
    def animate(i,x,y):
        
        argSensor1 = firstsensor.init()
        
        x.append(dt.datetime.now().strftime('%H:%M:%S'))
        y.append(firstsensor.read_temp1(argSensor1))
        
        # Limit x and y lists to 20 items
        x = x[-10:]
        y = y[-10:]
        
        total = sum(y)
        average_temp = round(total/len(y),2)
        print("Average temperture last ten second : ",average_temp," degree celsius")

        # Draw x and y lists
        axes.clear()
        plt.xticks(rotation=45, ha='right')
        axes.set_ylabel('Temperature in Celsius')
        axes.set_xlabel('Time (Second)')
        axes.set_title('Graph of temperature')

        plt.plot(x, y, scaley=True, scalex=True, color="blue")
        time.sleep(0.001)

    ani = FuncAnimation(fig=fig, func=animate, init_func=lambda: None,fargs=(x, y), interval=1000, save_count=10000)
    plt.show()

except:
    exit()