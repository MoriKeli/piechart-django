from django.shortcuts import render

# Python modules
import matplotlib.pyplot as plt
import random
import matplotlib
import numpy as np

matplotlib.use('Agg')   # A UserWarning Error will be raised if this is excluded.


def piechart(request):
    # piechart, where the slices will be ordered and plotted counter-clockwise:

    labels = 'Sale', 'Purchase', 'Loss'
    sizes = [random.randint(10, 30), random.randint(30, 50), random.randint(30, 80)]    # dynamic values can also be used

    # 0.1 rep. slice 1: Sale; 0 the second slice: Purchase; 0 the 3rd slice: Loss 
    explode = (0.1, 0, 0)  # only "explode" the 1st slice(i.e. 'Sale')

    fig1, ax1 = plt.subplots()
    
    # value of keyword autopct should be enclosed between two % symbols, e.g. 1.2f -> %1.2f%%
    # startangle can have different values ranging from 0 - 360deg
    ax1.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", shadow=True, startangle=720)
    ax1.axis('equal')   # equal aspect ratio ensured that pie is drawn as a circle

    # Supported picture formats: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
    plt.savefig('media/piechart.png', dpi=100)

    return render(request, 'app/index.html')
