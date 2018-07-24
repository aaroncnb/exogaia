#!/usr/bin/python

from numpy import *
import matplotlib.pyplot as plt
import sys

time = []
pop = []
temp = []
with open("exogaia_macro_data_"+str(sys.argv[1])+".txt") as data:
	for dat in data:
		line = str.split(dat)
		time.append(int(line[0]))
		pop.append(double(line[1]))
		temp.append(double(line[4]))

fig1 = plt.figure(figsize=(10,6),dpi=100)
plt.rcParams['xtick.labelsize'] = 18;
plt.rcParams['ytick.labelsize'] = 18;
ax1 = fig1.add_subplot(111);
plt.xlabel('timestep', fontsize=28)
plt.plot(time,temp,'-r',label='temperature')
ax1.set_ylabel('temperature (red)', fontsize=28)
#plt.ylim(800,1200);

plt.axhline(y=1000,xmin=0,xmax=250000,c="green",linewidth=1.,zorder=0,label='microbe ideal temperature')

ax2 = fig1.add_subplot(111, sharex=ax1, frameon=False)
plt.plot(time,pop,'-b')
ax2.set_ylabel('population (blue)', fontsize=28)
ax2.yaxis.tick_right();
ax2.yaxis.set_label_position('right')
plt.xlim(0,500000)

#plt.legend(loc=1,prop={'size':20})
plt.tight_layout()

plt.show();




