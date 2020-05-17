#Import Necessary Libraries
import chartmogul
import json
import datetime
import pandas as pd

def connect():
    #Implemented this way for simplicity
    with open('creds.json') as f:
        creds = json.load(f)
        f.close()
    
    #Connect to Chart Mogul
    config = chartmogul.Config(**creds)
    return config

def mrr_cleaner(result, df, interval):
    for entry in result.entries:
        df=df.append({'end_date': entry.date.strftime('%Y-%m-%d'), 
                      'interval':interval,
                      'mrr': entry.mrr,
                      'mrr_churn': entry.mrr_churn,
                      'mrr_contraction': entry.mrr_contraction,
                      'mrr_expansion': entry.mrr_expansion,
                      'mrr_new_business': entry.mrr_new_business,
                      'mrr_reactivation': entry.mrr_reactivation}, ignore_index=True)
    df['mrr_positive'] = df['mrr_expansion'] + df['mrr_new_business'] + df['mrr_reactivation']
    df['mrr_negative'] = df['mrr_churn'] + df['mrr_contraction']
    return df

def main():
    #Dataframe to visualize Customer List
    column_names = ['end_date','interval','mrr','mrr_churn','mrr_contraction','mrr_expansion','mrr_new_business','mrr_reactivation']
    df = pd.DataFrame(columns = column_names)
    #Connection Call
    config = connect()
    
    interval = 'month' # day, week, month, or quarter - change as needed
    start_date = '2020-01-01' #change as needed format (yyyy-mm-dd)
    end_date = '2020-04-30' #change as needed (yyyy-mm-dd)
    
    result = chartmogul.Metrics.mrr(
        config,
        start_date=start_date,
        end_date=end_date,
        interval=interval).get()
    #Format the data
    df = mrr_cleaner(result, df, interval)
    #Save the data into a csv
    df.to_csv('mrr_data.csv',index=False)
    
    ax = df[['end_date', 'mrr']].plot(x='end_date', linestyle='-', marker='o',colormap='hsv')
    df[['end_date', 'mrr_positive','mrr_negative']].plot(x='end_date', kind='bar',stacked = True, ax=ax)

if __name__ == "__main__":
    main()
