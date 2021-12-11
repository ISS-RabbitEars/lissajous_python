import math
import matplotlib.pyplot as plt
from matplotlib import animation

def setplot1(sx,sy):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-sx,sx])
	plt.ylim([-sy,sy])
	ax.set_facecolor('xkcd:black')

def setplot2(sx1,sx2,sy1,sy2):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([sx1,sx2])
	plt.ylim([sy1,sy2])
	ax.set_facecolor('xkcd:black')

frps=30
sec=5
fs=frps*sec
nx=5
ny=5
N=1000
dt=2*math.pi/N
delta=2*math.pi/fs
t=[]
x=[]
y=[]
for i in range(N+1):
	t.append(i*dt)
	x.append(0)
	y.append(0)

def lc(xm,wx,dx,ym,wy,dy,t,n):
	x1=[]
	y1=[]
	for i in range(n+1):
		x1.append(xm*math.sin(wx*t[i]-dx))
		y1.append(ym*math.sin(wy*t[i]-dy))
	return x1,y1
	

fig, a=plt.subplots()

w1=0
w2=-1
def run(frame):
	global x,y,w1,w2
	plt.clf()
	if (frame%(nx*fs)==0):
		w1=0
		w2+=1
	if (frame%fs==0):
		w1+=1
	x,y=lc(1,w1,-frame*delta,1,w2,0,t,N)
	plt.plot(x,y,color='r')
	setplot1(1.2,1.2)	
	plt.suptitle('Lissajous Curves')
	plt.title(r'$\omega_{x}='+str(w1)+' ,\omega_{y}='+str(w2)+'$')

ani=animation.FuncAnimation(fig,run,interval=1,frames=nx*ny*frps*sec)
writervideo = animation.FFMpegWriter(fps=frps)
ani.save('lissajous.mp4', writer=writervideo)
plt.show()

