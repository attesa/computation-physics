program WH_BUTTERFLY
real,external :: f1,f2,f3
real :: k1,k2,k3,k4,l1,l2,l3,l4,m1,m2,m3,m4,x,y,z,t
real :: x0,y0,z0
real,parameter :: h=0.0001
real :: t1,t2
integer :: i,n
open (unit=8,file='wh_butterfly.txt')
t=0
n=1000000
write(*,*)"give x0,y0,z0"
read(*,*)x0,y0,z0
call cpu_time(t1)
do i=1,n,1
write(8,*) x0,y0,z0
k1=f1(x0,y0)
l1=f2(x0,y0,z0)
m1=f3(x0,y0,z0)
k2=f1(x0+h/2*k1,y0+h/2*l1)
l2=f2(x0+h/2*k1,y0+h/2*l1,z0+h/2*m1)
m2=f3(x0+h/2*k1,y0+h/2*l1,z0+h/2*m1)
k3=f1(x0+h/2*k2,y0+h/2*l2)
l3=f2(x0+h/2*k2,y0+h/2*l2,z0+h/2*m2)
m3=f3(x0+h/2*k2,y0+h/2*l2,z0+h/2*m2)
k4=f1(x0+h*k3,y0+h*l3)
l4=f2(x0+h*k3,y0+h*l3,z0+h*m3)
m4=f3(x0+h*k3,y0+h*l3,z0+h*m3)
x=x0+1/6.0*(k1+2*k2+2*k3+k4)*h
y=y0+1/6.0*(l1+2*l2+2*l3+l4)*h
z=z0+1/6.0*(m1+2*m2+2*m3+m4)*h
t=t+h
x0=x
y0=y
z0=z
end do
call cpu_time(t2)
write(*,*)"THE RESULT HAS BEEN WRITEN IN THE TXT FILE"
write(*,*)t2-t1
stop
end 

real function f1(x,y)
real x,y
real :: a=10.0
f1=a*(y-x)
return
end

real function f2(x,y,z)
real x,y,z
real :: c=28
f2=c*x-y-x*z
return
end

real function f3(x,y,z)
real x,y,z
real :: b=8.0/3.0
f3=-b*z+x*y
return
end
