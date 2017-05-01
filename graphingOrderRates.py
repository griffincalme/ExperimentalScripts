import matplotlib.pyplot as plt
import numpy as np

initial_conc = 1000 #mg
time = 100 #mins

#noyes_whitney
#hixson_crowell
#higuchi


zero_order_rate = 10 #mg/min
zo_conc = [initial_conc] #zero order concentrations

first_order_rate = .10 #percent/min
fo_conc = [initial_conc] #first order concentrations
timepoints = [0]

for t in range(1,time):
    zo_conc.append(initial_conc - t*zero_order_rate)
    if t == 1:
        fo_conc.append(initial_conc - (initial_conc * first_order_rate))
    else:
        fo_conc.append((fo_conc[-1:][0]) - ((fo_conc[-1:][0]) * first_order_rate))
    timepoints.append(t)

#print(timepoints)
#print(zo_conc)
#print(fo_conc)

#slope_zo, intercept_zo = np.polyfit(timepoints , zo_conc, 1)
#print(slope_zo, intercept_zo)
#slope_fo, intercept_fo = np.polyfit(timepoints, fo_conc, 1)
#print(slope_fo, intercept_fo)

fo_slope = []
for i in fo_conc:
    #print(i)
    #print(fo_conc.index(i))
    #if fo_conc
    try:
        #print(fo_conc[fo_conc.index(i)+1])
        #print(fo_slope)
        fo_slope.append((fo_conc[fo_conc.index(i)+1] - fo_conc[fo_conc.index(i)])*-1)
    except:
        pass

zo_slope = []
for i in zo_conc:
    #print(i)
    #print(fo_conc.index(i))
    #if fo_conc
    try:
        #print(fo_conc[fo_conc.index(i)+1])
        #print(fo_slope)
        zo_slope.append((zo_conc[zo_conc.index(i)+1] - zo_conc[zo_conc.index(i)])*-1)
    except:
        pass



t = np.arange(time)

fig, axes = plt.subplots(2, 2, figsize=(12, 11))
ax0, ax1, ax2, ax3 = axes.ravel()

ax0.plot(t, zo_conc)
ax0.plot(t, fo_conc)
ax0.set_title("Concentration [x]")
ax0.legend(['y = ZO', 'y = FO'], loc='upper left')

ax1.plot(t, zo_conc)
ax1.plot(t, fo_conc)
ax1.set_title("log of conc")
ax1.set_yscale('log', nonposy='clip')
ax1.legend(['y = ZO', 'y = FO'], loc='upper left')

ax2.plot(range(len(zo_slope)), zo_slope)
ax2.plot(range(len(fo_slope)), fo_slope)
ax2.set_title("d[x]/dt (release rate)")
#ax2.set_yscale('log', nonposy='clip')
ax2.legend(['y = ZO', 'y = FO'], loc='upper left')

ax3.plot(range(len(zo_slope)), zo_slope)
ax3.plot(range(len(fo_slope)), fo_slope)
ax3.set_title("log of d[x]/dt (release rate)")
ax3.set_yscale('log', nonposy='clip')
ax3.legend(['y = ZO', 'y = FO'], loc='upper left')

for ax in axes.ravel():
    ax.axis('on')

fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)



plt.show()
