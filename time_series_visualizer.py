import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = q1 = df['page_views'].quantile(0.025)
q3 = df['page_views'].quantile(0.975)
df_filtered = df.query('page_views >= @q1 and page_views <= @q3')

def draw_line_plot():
    # Draw line plot

    df_copy = df_filtered.copy()  # Indent to match the function's block
    fig, ax = plt.subplots(figsize=(12, 6))  # Same indentation level
    ax.plot(df_copy.index, df_copy['page_views'])  # Same level
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")  # Same level
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.xticks(rotation=45)

    plt.tight_layout()  # This needs to be indented to match the block

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')  
    return fig  

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_copy = df_filtered.copy()  
    df_grouped = df_copy.resample('M').mean()

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(10, 6))
    df_grouped.unstack().plot(kind='bar', ax=ax)
    ax.set_title("Months")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    sns.boxplot(
        x="year", y="page_views", showmeans=True, data=df_copy, ax=ax1
    )
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45) 

    sns.boxplot(
        x="month", y="page_views", showmeans=True, data=df_copy, ax=ax2
    )
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    plt.xticks(rotation=45)  
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
