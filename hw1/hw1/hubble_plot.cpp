#include <cstdlib>  // to use system function
#include <fstream>
using std::ofstream;
#include <iostream>
using std::cerr;
using std::endl;
#include <string>
using std::string;

#ifdef WIN32
    string gnuplot = "\"C:\\Program Files\\gnuplot\\bin\\wgnuplot.exe\" ";
#elif __CYGWIN__
    string gnuplot = "/cygdrive/c/gnuplot/binary/wgnuplot.exe ";
#else
    string gnuplot = "gnuplot ";
#endif

const int n = 24;   // number of galaxies in Table 1

double r[n] = {     // distances in Mpc
    0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, 0.8, 0.9,
    0.9,   0.9,   0.9,   1.0,   1.1,   1.1,   1.4,  1.7, 2.0, 2.0,  2.0, 2.0
};

double v[n] = {     // velocities in km/s
    +170, +290, -130, -70,  -185, -220, +200, +290, +270, +200, +300, -30,
    +650, +150, +500, +920, +450, +500, +500, +960, +500, +850, +800, +1090
};

int main()
{
    // open a file to write Hubble's data
    ofstream file("hubble.dat");

    // write the data r, v data pairs
    for (int i = 0; i < n; i++)
        file << r[i] << '\t' << v[i] << '\n';

    // close the data file
    file.close();

    // open a file for data in LaTeX table row format
    file.open("hubble_table.tex");
    for (int i = 0; i < n; i++)
        file << r[i] << " & " << v[i] << " \\\\" << '\n';
    file.close();

    // open a file for Gnuplot commands
    file.open("hubble.gnu");

    // write Gnuplot commands on separate lines
    file << "set terminal postscript" << endl
         << "set output \"hubble_plot.eps\"" << endl
         << "set title \"Figure 1\"" << endl
         << "set xlabel \"r (Mpc)\"" << endl
         << "set ylabel \"v (km/s)\"" << endl
         << "f(x) = a + b*x" << endl
         << "set fit logfile" << endl
         << "fit f(x) \"hubble.dat\" via a, b" << endl
         << "set label \"a = %g\", a at 1.5, -100" << endl
         << "set label \"b = %g\", b at 1.5, -200" << endl
         << "plot \"hubble.dat\", f(x) title \"v(r)=a+br\"" << endl;

    // plot the data
    string command = gnuplot + "hubble.gnu";
    int return_value = system(command.c_str());
    if (return_value != 0) {
        cerr << "system(" << command << ") failed" << endl;
        exit(1);
    }
}
