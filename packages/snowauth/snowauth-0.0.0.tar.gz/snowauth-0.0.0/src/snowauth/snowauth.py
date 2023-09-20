import os
#import toml
#from snowflake.snowpark.session import Session

#HOME = os.path.expanduser('~')
#CREDS_PATH = os.path.join(HOME, '.snowauth', 'creds.conf')

#with open(CREDS_PATH, 'r') as f:
    #conf = toml.load(f)

def connect(connection_name):
    print(connection_name)