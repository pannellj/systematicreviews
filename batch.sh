#!/bin/bash
for file in *.pdf; do
	name=${file##*/}
	outfile=${name%.*}
	pdftotext $file $outfile.txt;
done
