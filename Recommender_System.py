

# Importing training json data to pandas 
import json
from pprint import pprint
import pandas as pd

with open('training_mixpanel.txt') as f:
    data = json.load(f)

for result in data:
    # Separating the attributes like [invoice_no, product_id, ...] from properties attribute of json file.
    result[u'invoice_no']=result[u'properties'][u'invoice_no'] 
    result[u'product_id']=result[u'properties'][u'product_id']
    result[u'description']=result[u'properties'][u'description']
    result[u'quantity']=result[u'properties'][u'quantity']
    result[u'unit_price']=result[u'properties'][u'unit_price']
    result[u'customer_id']=result[u'properties'][u'customer_id']
    result[u'country']=result[u'properties'][u'country']

    del result[u'properties']  # deleting the [properties] attribute in the json

purchase_history = json.dumps(data)
pd.read_json(purchase_history)

## Confirming the Event types available
df = pd.DataFrame(data)
df.event.unique()   