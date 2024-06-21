import sqlalchemy as db
import pandas as pd

# Convert a CSV file to a SQL table
engine = db.create_engine("sqlite:///datacamp.sqlite")

df = pd.read_csv('indexData.csv')
df.to_sql(con=engine, name="Stock price", if_exists='replace', index=False)

# Validate results by connecting to database
conn = engine.connect()
metadata = db.MetaData()

# Make table object
stock = db.Table('Stock price', metadata, autoload_with=engine)

# Execute the query and display results
query = stock.select()
exe = conn.execute(query)
result = exe.fetchmany(5)
for r in result:
    print(r)

# Update values in table
# update, values, and where functions
stock.update().values(column_1=1, column_2=4).where(stock.columns.column_5 >= 5)

# Delete records in table
stock.delete().where(stock.columns.column_5 >= 5)

# Validate results
output = conn.execute(stock.select()).fetchall()
data = pd.DataFrame(output, columns=['Column 1', 'Column 2', 'Column 3'])
print(data)

results.close()
exe.close()