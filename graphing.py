import matplotlib.pyplot as plt

time = [0.0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
position = [0.0, 1.1,3.2,5.7,8.9,12.7,17,22,27.4]

velocity = [0.0, 16,23,28.5,35,40.5,46.5,52,0.0]
time2 = [0.0, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]

plt.plot(time, position, label = 'position', color = 'green', linewidth = 3, marker = 'o', markerfacecolor = 'blue')
plt.plot(time2, velocity, label = 'velocity', color = 'blue', linewidth = 3, marker = 'o', markerfacecolor = 'green')
plt.xlabel('Time(s)')
plt.ylabel('Position(cm)/velocity(cm)')
plt.legend()


plt.title("Position, d of a Fletcher Trolly Cart "
          "Accelerating across a plane at \n59.6 m/s^2[E] "
          "due to the hanging mass of 100g as a function of time,s")



plt.show()


