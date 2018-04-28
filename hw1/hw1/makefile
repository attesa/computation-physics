# hash character comments the rest of the line

ifeq ($(OS), Windows_NT)
    exe = hubble_plot.exe
else
    exe = hubble_plot
endif

plots = hubble_plot.png             # list of plot files

all : hw1.pdf ;                     # all : targets to be made

hw1.pdf : hw1.tex $(plots)          # target needs (:) .tex and image files
	pdflatex hw1.tex                # command line MUST start with TAB !!!!
	pdflatex hw1.tex                # run again to resolve references

$(plots) : $(exe)                   # plots need executable
	./$(exe)                        # run the executable

$(exe) : hubble_plot.cpp            # executable needs code file
	c++ -o $@ $<                    # $@ = target, $< = first need file
