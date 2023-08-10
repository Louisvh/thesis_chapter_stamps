#!/bin/bash

thesis_file=${1:-dummy_thesis.pdf}
temp_file=tmp_$1
cp $thesis_file $temp_file

read -e -p "Enter bleed in mm: " -i "0" BLEED

python create_stamps.py $BLEED

for l in `cat chapter_pages.txt`; 
do 
    chapter=${l%:*}
    chaprange=${l#*:}
    mstamp="stamp_$chapter.pdf"
    echo $mstamp

    # append an empty page (stamp 0), as we only want to stamp every other page
    qpdf $mstamp --pages $mstamp 1 stamp_0.pdf 1 -- stamp_full.pdf

    qpdf $temp_file --underlay stamp_full.pdf --to=$chaprange --repeat=1,2 -- --replace-input
done

mv $temp_file result_$thesis_file
echo wrote result_$thesis_file
rm stamp*.pdf
