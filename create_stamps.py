import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches

if len(sys.argv) < 2:
    print('usage: python create_stamps.py bleed_in_millimetres')
    quit()

bleed_mm = float(sys.argv[1])
starty = bleed_mm + 36
yincrement = 12
stamp_height = 12
stamp_width = 12+bleed_mm
pagex, pagey = 170+2*bleed_mm, 240+2*bleed_mm
xloc = pagex - stamp_width
mfontsize = 20
mfontdict = None
mfontdict = {'fontfamily': 'Garuda'}

def create_stamp(i):
    mm = 1/25.4
    plt.figure(figsize=(pagex*mm, pagey*mm))
    ax = plt.gca()
    ax.set_axis_off()
    plt.xlim([0, pagex])
    plt.ylim([0, pagey])
    yloc = pagey-(starty + i*yincrement)
    if i>0: #create empty page as well
        mrect = patches.Rectangle((xloc, yloc), stamp_width, stamp_height, facecolor = 'gray', fill=True)
        ax.add_patch(mrect)
    plt.text(x=xloc+6,y=yloc+5.5,s=str(i), c='w', va='center', ha='center', fontsize=mfontsize, fontdict=mfontdict)

    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0,hspace = 0, wspace = 0)
    plt.margins(0,0)
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(f'stamp_{i}.pdf', bbox_inches = 'tight', pad_inches = 0)
   
for i in range(20):
    create_stamp(i)

