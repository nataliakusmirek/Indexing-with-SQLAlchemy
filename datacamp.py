import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///datacamp.sqlite')
conn = engine.connect()
metadata = db.MetaData()


# Create the structure of the table
Student = db.Table('Student', metadata,
                   db.Column('Id', db.Integer, primary_key=True),
                   db.Column('Name', db.String(50), nullable=False),
                   db.Column('Major', db.String(50), default="Math"),
                   db.Column('Pass', db.Boolean(), default=True)
                   )

metadata.create_all(engine)

# Insert one row
query = db.insert(Student).values(Id=1, Name="John", Major="Math", Pass=True)
result = conn.execute(query)

# Double check the row has been successfully added
output = conn.execute(Student.select()).fetchall()
print(output)

# Insert many rows
query = db.insert(Student)
values_list = [{"Id": 2, "Name": "Ham", "Major": "Spanish", "Pass": False},
               {"Id": 3, "Name": "James", "Major": "History", "Pass": True},
               {"Id": 4, "Name": "Riley", "Major": "Math", "Pass": False}]
result = conn.execute(query, values_list)

# Double check the rows have been successfully added
output = conn.execute(Student.select()).fetchall()
print(output)



# Simple SQL query with SQLAlchemy is possible by having the query be in ""
#output = conn.execute("SELECT * FROM Student")
#print(output.fetchall())


# Using SQLALchemy API

# Apply AND logic to the WHERE query
query = Student.select().where(db.and_(Student.columns.Major == 'Math', Student.columns.Pass != True))
output = conn.execute(query)
print(output.fetchall())

# Output to Pandas DataFrame
query = Student.select().where(Student.columns.Major == 'History')
output = conn.execute(query)
results = output.fetchall()

data = pd.DataFrame(results, columns=Student.c.keys())
print(data)