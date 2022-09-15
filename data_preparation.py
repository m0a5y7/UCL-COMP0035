import pandas as pd

def set_pandas_display_options(df):
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)

def prepare_data(df):
    df.drop(['gla_id', 'species_name', 'common_name', 'load_date'], axis=1, inplace=True)
    df.fillna({'display_name': 'Other', 'borough': 'Unknown'}, inplace=True)
    df.dropna(inplace=True)

    df_ready = df

    return df_ready

def prepare_data_2(df):
    df.drop(['Qualifier', 'DataSource', 'DataVersion', 'ReleaseDate', 'Copyright', 'SiteID'], axis=1, inplace=True)
    df.fillna({'SiteName': 'Unknown', 'Borough': 'Unknown', 'PrimaryUse': 'Other'}, inplace=True)
    df.dropna(inplace=True)

    df_ready = df

    return df_ready

if __name__ == '__main__':

    # Trees dataset
    df = pd.read_csv('london_street_trees_gla_20180214.csv', encoding= 'unicode_escape',
                     dtype={'common_name': str, 'borough': str, 'display_name':str,
                            'easting':float, 'northing':float, 'longitude':float, 'latitude':float})

    df_prepared = prepare_data(df)
    set_pandas_display_options(df)

    # Everything fine here
    #print(df['display_name'].unique())
    #print(df['borough'].unique())

    # Open space dataset
    df2 = pd.read_csv('GiGL_openspace_subset_(beta)_V6.csv',
                      dtype= {'SiteName': str, 'PrimaryUse': str, 'Borough': str,
                              'AreaHa': float, 'Easting': float, 'Northing': float}, engine = 'python')

    df2_prepared = prepare_data_2(df2)

    set_pandas_display_options(df2)

    # Note: The boroughs are marked differently than in the tree dataset, and there are some cases where
    # the borough field marks two different boroughs (e.g. 'Hackney; Haringey'). This is a problem with the original dataset
    # and not a formatting issue. I am assuming the reason for this is that the open spaces go through all of the boroughs
    # mentioned. A short-term solution would be to remove all rows with ';' in the borough column, but I may need this
    # data in the final product. So instead, I will just be mindful of this in the exploration step.
    #print(df2['Borough'].unique())

    # I have decided not to merge these two datasets in the preparation step. Their number of rows are way too different,
    # and I don't think adding them into one dataset will add any value for the exploration.

    df_prepared.to_csv('/Users/marjaana/PycharmProjects/coursework-1-m0a5y7/London_trees_cleaned.csv')
    df2_prepared.to_csv('/Users/marjaana/PycharmProjects/coursework-1-m0a5y7/Openspace_cleaned.csv')






