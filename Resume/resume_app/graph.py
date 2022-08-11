import matplotlib

matplotlib.use('Agg')
from matplotlib import pyplot as plt
from io import StringIO
import pandas
import numpy
from django.templatetags.static import static


lbcolor = '#000000'

def ammount_trained():
    plt.rcParams['figure.figsize'] = (12, 5)

    #removed color
    #fig, ax = plt.subplots(facecolor=bgcolor)
    fig, ax = plt.subplots()

    # pandas func
    df = pandas.read_csv(static('Training_Numbers.csv'))

    df = df.sort_values('sort_key').reset_index(drop=True)

    # Values for PLot
    c = df['color']
    x = df['Dept']
    y = df['Count']

    # Bar PLot
    bars = plt.bar(x, height=y, width=0.8, bottom=None, align='center', data=None, color=c)
    # ['purple', 'blue', 'red']
    # Axis Forming
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(lbcolor)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=lbcolor)
    ax.xaxis.grid(False)

    # Grab the color of the bars so we can make the
    # text the same color.
    bar_color = bars[1].get_facecolor()

    # Add text annotations to the top of the bars.
    # Note, you'll have to adjust this slightly (the 0.3)
    # with different data.
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            round(bar.get_height(), 1),
            horizontalalignment='center',
            color=lbcolor,
            weight='bold'
        )

    # Add labels and a title. Note the use of `labelpad` and `pad` to add some
    # extra space between the text and the tick labels.
    """ax.set_xlabel('Level of Care', labelpad=15, color=lbcolor, backgroundcolor=bgcolor)
    ax.set_ylabel('Patient Count', labelpad=15, color=lbcolor, backgroundcolor=bgcolor)
    ax.set_title('Patients by Level of Care', pad=15, color=lbcolor,
                 weight='bold', backgroundcolor=bgcolor)
    ax.margins(0)
    ax.set_facecolor(color=bgcolor)"""

    ax.set_xlabel('Department', labelpad=15, color=lbcolor)
    ax.set_ylabel('Count of Trained', labelpad=15, color=lbcolor)
    ax.set_title('Count of New Hires Trained', pad=15, color=lbcolor,
                 weight='bold')
    ax.margins(0)
    #ax.set_facecolor()

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg', transparent=True)
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data