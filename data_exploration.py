import pandas as pd
import matplotlib.pyplot as plt

def set_pandas_display_options(df):
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)

#def compare_green_open(srs, srs2):


if __name__ == '__main__':
    df = pd.read_csv('London_trees_cleaned.csv')
    set_pandas_display_options(df)

    df2 = pd.read_csv('Openspace_cleaned.csv')
    set_pandas_display_options(df2)

    # How many trees each borough has
    print(df['borough'].value_counts())

    df['borough'].value_counts().plot(kind = 'bar')
    plt.show()

    # Which borough has the least open space
    print(df2['Borough'].value_counts())

    # Making a histogram
    df2['Borough'].value_counts().plot(kind='bar')
    plt.show()

    # NOTE: If I had not run out of time with this coursework, I would have created a function that does this comparison
    # and joins the two dataframes at the end
    # Finding out what type of open space the 5 least green boroughs have
    trees = df['borough'].value_counts(ascending=True)[:5].to_frame()

    # For df2, I need info about boroughs, and primary use
    os = df2[(df2['Borough'].isin(['City of London','Kensington and Chelsea', 'Bexley', 'Lambeth', 'Tower Hamlets']))]

    os.drop(['SiteName', 'AreaHa', 'Easting', 'Northing'], axis=1, inplace=True)

    nos = os.groupby('Borough')['PrimaryUse'].agg(['unique'])

    trees.join(nos.set_index('Borough'), on='Borough')






