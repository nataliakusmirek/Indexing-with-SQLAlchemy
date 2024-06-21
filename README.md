# Indexing-with-SQLAlchemy

This repository contains code and examples to practice the concepts covered in the [DataCamp SQLAlchemy tutorial](https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples). The tutorial covers various aspects of SQLAlchemy, including creating tables, inserting data, querying, and more.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. This repository provides practical examples and exercises to help you get hands-on experience with SQLAlchemy.

## Setup

To get started, clone the repository and set up your virtual environment:

```sh
git clone https://github.com/yourusername/sqlalchemy-tutorial-practice.git
cd sqlalchemy-tutorial-practice
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage

The repository includes several Python scripts that demonstrate different SQLAlchemy concepts. You can run these scripts to see the examples in action.

### Examples

1. **Creating and Reflecting Tables**
    ```python
    import sqlalchemy as db

    engine = db.create_engine('sqlite:///datacamp.sqlite')
    conn = engine.connect()
    metadata = db.MetaData()

    # Define and create the Student table
    Student = db.Table('Student', metadata,
                       db.Column('Id', db.Integer, primary_key=True),
                       db.Column('Name', db.String(50), nullable=False),
                       db.Column('Major', db.String(50), default="Math"),
                       db.Column('Pass', db.Boolean(), default=True)
                      )
    metadata.create_all(engine)

    # Insert data into the Student table
    query = db.insert(Student).values(Id=1, Name="John", Major="Math", Pass=True)
    result = conn.execute(query)

    # Query the Student table
    query = Student.select()
    results = conn.execute(query).fetchall()
    for result in results:
        print(result)
    ```

2. **Joining Tables and Advanced Queries**
    ```python
    query = db.select(
        [division.c.Div, match.c.HomeTeam, match.c.AwayTeam]
    ).select_from(
        division.join(match, division.c.Division == match.c.Div)
    ).where(
        db.and_(division.c.Division == "E1", match.c.Season == 2009)
    ).order_by(
        match.c.HomeTeam
    )

    output = conn.execute(query)
    results = output.fetchall()

    # Convert results to a DataFrame
    data = pd.DataFrame(results, columns=['Div', 'HomeTeam', 'AwayTeam'])
    print(data)
    ```

3. **More Examples**
    - `insert_data.py`: Script to insert data into tables.
    - `query_data.py`: Script to perform various queries on the database.
    - `advanced_queries.py`: Script to demonstrate advanced SQL queries with SQLAlchemy.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add your feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a pull request
