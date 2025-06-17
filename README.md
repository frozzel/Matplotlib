# Matplotlib
Data Visualisation with Matplotlib

## Get the Data
Either use the provided .csv file or (optionally) get fresh (the freshest?) data from running an SQL query on StackExchange:

Follow this link to run the query from StackExchange to get your own .csv file

select dateadd(month, datediff(month, 0, q.CreationDate), 0) m, TagName, count(*) from PostTags pt join Posts q on q.Id=pt.PostId join Tags t on t.Id=pt.TagId where TagName in ('java','c','c++','python','c#','javascript','assembly','php','perl','ruby','visual basic','swift','r','object-c','scratch','go','swift','delphi') and q.CreationDate < dateadd(month, datediff(month, 0, getdate()), 0) group by dateadd(month, datediff(month, 0, q.CreationDate), 0), TagName order by dateadd(month, datediff(month, 0, q.CreationDate), 0)

## Import Statements

```python
    pip3 install pandas
```


## Data Exploration
Read the .csv file and store it in a Pandas dataframe

```python
load_data(file_path)
```

Examine the first 5 rows and the last 5 rows of the of the dataframe

```python
head()
tail()
```

Check how many rows and how many columns there are. What are the dimensions of the dataframe?

```python
shape()
```

Count the number of entries in each column of the dataframe

```python
shape[0]
shape[1]
```

Calculate the total number of post per language. Which Programming language has had the highest total number of posts of all time?

```python
groupby('TAG').sum()
```

Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.

How many months of data exist per language? Which language had the fewest months with an entry?


[ ]

Start coding or generate with AI.
Data Cleaning
Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"


[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.
Data Manipulation

[ ]

Start coding or generate with AI.
Challenge: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe.


[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.
Challenge: Count the number of entries per programming language. Why might the number of entries be different?


[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.
Data Visualisaton with with Matplotlib
Challenge: Use the matplotlib documentation to plot a single programming language (e.g., java) on a chart.


[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.

[ ]

Start coding or generate with AI.
Challenge: Show two line (e.g. for Java and Python) on the same chart.


[ ]

Start coding or generate with AI.
Smoothing out Time Series Data
Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: rolling() and mean().


[ ]

[ ]

[ ]

[ ]
Colab paid products - Cancel contracts here

