import sqlalchemy as db
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Create a SQLLite engine to work with and connect to it!
engine = db.create_engine('sqlite:///european_database.sqlite')

conn = engine.connect()

# Create a table object: requires table names and metadate

metadata = db.MetaData() # extracting the metadata
division = db.Table('divisions', metadata, autoload_with=engine)
match = db.Table('matchs', metadata, autoload_with=engine)


# Print table metadata to see the table name, columns names and type, and schema
print(repr(metadata.tables['divisions']))

# Print column names
print(division.columns.keys())



# RUN QUERIES
query = division.select() # SELECT * FROM divisions
print(query) # prints the equivalent SQL command

# fetchone() extracts a single row at a time
# fetchmany(n) extracts n rows at a time
# fetchall() extracts all rows

exe = conn.execute(query) # executing the query using an execute object
result = exe.fetchmany(5)

# Result is first 5 rows of the table
print(result)


query = db.select([division, match]).\
select_from(division.join(match, division.columns.division == match.columns.Div)).\
where(db.and_(division.columns.Div == "E1", match.columns.season == 2009)).\
order_by(match.columns.HomeTeam)
output = conn.execute(query)
results = output.fetchall()

data = pd.DataFrame(results, columns=['Div', 'HomeTeam', 'AwayTeam'])
print(data)


# VISUALIZE using MPL
sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(15,6))
plt.xticks(rotation=90)
sns.set_color_codes("pastel")
sns.barplot(x="HomeTeam", y='FTHG', data=data,
            label="Home Team Goals", color="b")

sns.barplot(x="AwayTeam", y='FTAG', data=data,
            label="Away Team Goals", color="r")

ax.legend(ncol=2, loc="upper left", frameon=True)
ax.set(ylabel="", xlabel="")
sns.despine(left=True, bottom=True)


# Save query results to a CSV through Pandas pipeline
output = conn.execute("SELECT * FROM matchs WHERE HomeTeam LIKE 'Norwich'")
results = output.fetchall()

data = pd.DataFrame(results, columns=['Div', 'HomeTeam', 'AwayTeam'])
# Avoid adding a column called "Index" by using "index=False"
data.to_csv("RESULTS.csv", index=False)