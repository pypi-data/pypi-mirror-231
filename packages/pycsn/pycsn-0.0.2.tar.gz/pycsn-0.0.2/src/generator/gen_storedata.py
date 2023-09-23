import pandas as pd
import numpy as np
import random
from os import path
from datetime import datetime
import argparse

def main():

    parser = argparse.ArgumentParser(prog='gen_storedata',
                                     description='Creates retail transactions for a store for testing.')
  
    parser.add_argument('-n', '--num_transactions', help='Number of transactions', type=int, default=1000)
    parser.add_argument('-i', '--id', help='store id', type=int, default=400)
    parser.add_argument('-s', '--start',help='Start date. Format="%Y-%M-%D, example="2021-01-01', default='2021-01-01') 
    parser.add_argument('-e', '--end',help='End date. Format="%Y-%M-%D, example="2021-01-01', default='2021-12-31') 
    args = parser.parse_args()

    store_id = args.id
    num_transactions = args.num_transactions
    start_date = args.start
    end_date = args.end
    filename = path.join('data', 'store_'+str(store_id)+'.csv')
    offset = random.randint(1000,10000)


    df_sizes = pd.read_csv('data/testdata_conf/sizes.csv',index_col='size')
    df = pd.read_csv('data/testdata_conf/products.csv')
    df_stores = pd.read_csv('data/testdata_conf/stores.csv',index_col='store_id')

    # get country
    country = df_stores.loc[store_id,'country']
    print(f'Country: {country}')

    # select products by country
    df = df[['article_id','category','name',country]]

    # select sizes by country
    df_sizes = df_sizes[[country]]
    df['size'] =[df_sizes.index.to_list()] * df.shape[0]
    size_share = df_sizes[country].to_list() * df.shape[0]
    df = df.explode('size')
    df['share'] = size_share
    df['share'] *= df[country] * num_transactions
    df['share'] = df['share'].astype('int32')

    df['store_id'] = store_id 
    df = df.apply(lambda x: x.repeat(df.share))

    # add date transactions
    start_date = np.datetime64(start_date)
    end_date = np.datetime64(end_date)
    num_days = (end_date - start_date).astype(int)
    # df['transaction_date'] = start_date + np.random.randint(0,num_days,df.shape[0])
    df['transaction_date'] = start_date + np.random.randint(0,num_days,df.shape[0]) * np.timedelta64(1,'D') + \
                             np.random.randint(28800,72000,df.shape[0]) * np.timedelta64(1,'s')
    df = df.sort_values(by='transaction_date')
    df = df[['store_id','article_id','category','name','size','transaction_date']]
    df = df.reset_index(drop=True).reset_index().rename(columns={'index': 'transaction_id'})
    df['transaction_id'] += offset

    df.to_csv(filename,index=False)

    # df[[article_id category     name   Germany sizes  share  store_id transaction_date]]


if __name__ == '__main__':
    main()