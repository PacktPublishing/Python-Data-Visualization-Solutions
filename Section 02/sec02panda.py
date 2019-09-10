data = pd.read_csv('sec02-data.csv')
data['amount_x_2'] = data['amount']*2
data.to_csv('sec02-data_more.csv)
print (data.amount)
print (data.columns)
Index([u'day', u'amount'], dtype='object')
pd.read_csv('sec02-data.tab', skiprows=1,
 delimiter=' *', names=['day','amount'])
