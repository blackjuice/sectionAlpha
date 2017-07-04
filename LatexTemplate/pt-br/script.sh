#! /bin/bash

rm draft.pdf # remove previous version

# compile .tex file
cd tex
latexmk -xelatex -f "draft.tex" > custom.log

# redirecting files and deleting temporary ones
mv *.pdf ../
rm *.bcf *.lof *.log *.lot *.xml *.aux *.fdb_latexmk *.fls *.out *.toc *.bbl *.blg
