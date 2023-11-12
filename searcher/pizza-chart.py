from bs4 import BeautifulSoup
import pandas as pd
from math import pi
from mplsoccer import Radar, FontManager, grid
from mplsoccer import PyPizza
import matplotlib.pyplot as plt


font_normal = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto%5Bwdth,wght%5D.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto-Italic%5Bwdth,wght%5D.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab%5Bwght%5D.ttf')

def playerRadar(playerName=None, statsList=None, statsValue=None):
    if not playerName:
        playerName = 'Levi Colwill'
    if not statsList:
        statsList = ['Non-Penalty Goals', 'Non-Penalty xG', 'Shots Total', 'Assists', 'xAG', 'npxG + xAG', 'Shot-Creating Actions',
                 'Passes Attempted', 'Pass Completion %', 'Progressive Passes', 'Progressive Carries', 'Successful Take-Ons',
                 'Touches (Att Pen)', 'Progressive Passes Rec', 'Tackles', 'Interceptions',
                 'Blocks', 'Clearances', 'Aerials won']
    if not statsValue:
        statsValue = [20, 95, 67, 99, 80, 93, 93, 99, 78, 92, 88, 19, 52, 51, 1, 37, 1, 12, 95]
    params = statsList
    values = statsValue
    statsLen = len(statsValue)

    # color for the slices and text
    slice_colors = ["#1A78CF"] * 7 + ["#FF9300"] * 7 + ["#D70232"] * 5
    text_colors = ["#000000"] * statsLen  # + ["#F2F2F2"] * 5

    # instantiate PyPizza class
    baker = PyPizza(
        params=params,                  # list of parameters
        background_color="#222222",     # background color
        straight_line_color="#000000",  # color for straight lines
        straight_line_lw=1,             # linewidth for straight lines
        last_circle_color="#000000",    # color for last line
        last_circle_lw=1,               # linewidth of last circle
        other_circle_lw=0,              # linewidth for other circles
        inner_circle_size=20            # size of inner circle
    )

    # plot pizza
    fig, ax = baker.make_pizza(
        values,                          # list of values
        # adjust the figsize according to your need
        figsize=(8, 8.5),
        color_blank_space="same",        # use the same color to fill blank space
        slice_colors=slice_colors,       # color for individual slices
        value_colors=text_colors,        # color for the value-text
        value_bck_colors=slice_colors,   # color for the blank spaces
        blank_alpha=0.4,                 # alpha for blank-space colors
        kwargs_slices=dict(
            edgecolor="#000000", zorder=2, linewidth=1
        ),                               # values to be used when plotting slices
        kwargs_params=dict(
            color="#F2F2F2", fontsize=8,
            fontproperties=font_normal.prop, va="center"
        ),                               # values to be used when adding parameter labels
        kwargs_values=dict(
            color="#F2F2F2", fontsize=11,
            fontproperties=font_normal.prop, zorder=3,
            bbox=dict(
                edgecolor="#000000", facecolor="cornflowerblue",
                boxstyle="round,pad=0.2", lw=1
            )
        )                                # values to be used when adding parameter-values labels
    )

    # add title
    fig.text(
        0.515, 0.975, playerName, size=16,
        ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
    )

    # add subtitle
    fig.text(
        0.515, 0.955,
        "Percentile Rank vs Top-Five League Defenders | Last 365 days",
        size=13,
        ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
    )

    # add credits
    CREDIT_1 = "data: statsbomb viz fbref"
    CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

    fig.text(
        0.99, 0.02, f"{CREDIT_1}\n{CREDIT_2}", size=9,
        fontproperties=font_italic.prop, color="#F2F2F2",
        ha="right"
    )

    # add text
    fig.text(
        0.34, 0.93, "Attacking        Possession       Defending", size=14,
        fontproperties=font_bold.prop, color="#F2F2F2"
    )

    # add rectangles
    fig.patches.extend([
        plt.Rectangle(
            (0.307, 0.927), 0.025, 0.021, fill=True, color="#1a78cf",
            transform=fig.transFigure, figure=fig
        ),
        plt.Rectangle(
            (0.47, 0.927), 0.025, 0.021, fill=True, color="#ff9300",
            transform=fig.transFigure, figure=fig
        ),
        plt.Rectangle(
            # (0.632, 0.9225), 0.025, 0.021, fill=True, color="#d70232",
            # transform=fig.transFigure, figure=fig
            (0.64, 0.927), 0.025, 0.021, fill=True, color="#d70232",
            transform=fig.transFigure, figure=fig
        ),
    ])

    plt.show()