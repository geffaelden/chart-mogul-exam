#Import Necessary Libraries
import chartmogul
import json
import datetime
import pandas as pd

#Importing for Sales Agent Randomness 
from random import randrange

def connect():
    #Implemented this way for simplicity
    with open('creds.json') as f:
        creds = json.load(f)
        f.close()
    
    #Connect to Chart Mogul
    config = chartmogul.Config(**creds)
    return config

def no_file_input(df):
    #Get Customer List
    result = chartmogul.Customer.all(config).get()
    
    #This loads data into the df for structure
    for customer in result.entries:
        df=df.append({'uuid': customer.uuid, 
                      'name':customer.name,
                      'external_id':customer.external_id}, ignore_index=True)
        
    #Loop through customer list table to assign sales agents 
    for uuid in df['uuid']:
        #find out assigned sales agent - Note: I could've explicit indicated who is assigned but I wanted to add randomness
        assigned_sales = sales[randrange(4)]
        #actual api call to add custom attribute
        chartmogul.CustomAttributes.add(
            config,
            uuid=uuid,
            data={
                'custom': [
                    {"type": "String", "key": "sales_agent", "value": assigned_sales}
                ]
            }
        )
        #Update Customer List Table
        df.loc[df['uuid']==uuid,'sales_agent']=assigned_sales
    return df

def with_file(file_input):
    for i in range(len(file_input)):
        #actual api call to add custom attribute
        chartmogul.CustomAttributes.add(
            config,
            uuid=file_input['uuid'][i],
            data={
                'custom': [
                    {"type": "String", "key": "sales_agent", "value": file_input['sales_agent'][i]}
                ]
            }
        )

def main():
    #Dataframe to visualize Customer List
    column_names = ['uuid','name','external_id']
    df = pd.DataFrame(columns = column_names)
    
    #Sales Agent List
    sales = ['Stephen Curry', 'Anfernee Hardaway','Tracy McGrady','Dwyane Wade']

    #Connection Call
    config = connect()
    
    try: 
        #This checks if you have a file input with your mapping of sales agent to customer.
        #Required file format is csv with the columns uuid and sales_agent. Other columns can be present but will be ignored.
        file_input = pd.read_csv('agent_mapping.csv')
        print('File found.')
        if 'uuid' in file_input and 'sales_agent' in file_input:
            with_file(file_input)
            df = file_input
        else: 
            print('One or both required columns not found. Please check your file and try again')
        
    except: 
        #No file input
        print('No file found.')
        print('Executing random assignment.')
        #This was done for random assignment of sales agent
        df = no_file_input(df)
        print('Done assignment')
        
    #Show final output of customer list with sales agent
    print(df)
    
if __name__ == "__main__":
    main()
