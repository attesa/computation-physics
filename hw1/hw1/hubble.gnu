set terminal postscript
set output "hubble_plot.eps"
set title "Figure 1"
set xlabel "r (Mpc)"
set ylabel "v (km/s)"
f(x) = a + b*x
set fit logfile
fit f(x) "hubble.dat" via a, b
set label "a = %g", a at 1.5, -100
set label "b = %g", b at 1.5, -200
plot "hubble.dat", f(x) title "v(r)=a+br"
