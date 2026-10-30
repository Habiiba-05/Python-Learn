# pandas - series

# 1
import pandas as pd

mylist = [100, 7, 13, 1]
series = pd.Series(mylist)
print(series)


print("-" * 50)


# 2
import pandas as pd

mylist = [100, 7, 13, 1]
series = pd.Series(mylist, index=["a", "b", "c", "d"])
series.iloc[1] = "H"
print(series.loc["a"])
print(series.iloc[1])


print("-" * 50)


# 3
import pandas as pd

mylist = [100, 7, 13, 1]
series = pd.Series(mylist, index=["a", "b", "c", "d"])
series.loc["b"] = "win"
print(series)


print("-" * 50)


# 4
import pandas as pd

people = {"rap": 3, "vocal": 4, "dancer": 7}
series = pd.Series(people)
print(series[series < 5])


print("-" * 50)


# pandas - dataframe (2D)


# 1
import pandas as pd 

people = {"name": ["jk", "v", "rm", "august D"],
          "age": [29, 30, 32, 33]
        }
df = pd.DataFrame(people)
print(df)


print("-" * 50)


# 2 
import pandas as pd 

people = {"name": ["jk", "v", "rm", "august D"],
          "age": [29, 30, 32, 33]
        }
df = pd.DataFrame(people, index=["member 1", "member 2", "member 3", "member 4"])

print(df)


print("-" * 50)


# 3
import pandas as pd 

people = {"name": ["jk", "v", "rm", "august D"],
          "age": [29, 30, 32, 33]
        }
df = pd.DataFrame(people, index=["member 1", "member 2", "member 3", "member 4"])
print(df.iloc[1])


print("-" * 50)


# 4 - add new column 
import pandas as pd 

people = {"name": ["jk", "v", "rm", "august D"],
          "age": [29, 30, 32, 33]
        }
df = pd.DataFrame(people, index=["member 1", "member 2", "member 3", "member 4"])
df["position"] = ["vocal 1", "vocal 2", "leader", "rapper"]
print(df)


print("-" * 50)


# 5 - add new row\s
import pandas as pd 

people = {"name": ["jk", "v", "rm", "august D"],
          "age": [29, 30, 32, 33]
        }

df = pd.DataFrame(people, index=["member 1", "member 2", "member 3", "member 4"])

df["position"] = ["vocal 1", "vocal 2", "leader", "rapper"]

new_Rows = pd.DataFrame([{"name": "jimin", "age": 31, "position": "dancer 1"},
           {"name": "hope", "age": 32, "position": "dancer 2 "}],
           index= ["member 5", "member 6"])
# i forget here the pd.DataFrame() 

df = pd.concat([df, new_Rows])
print(df)


print("-" * 50)


# importing
# can do exactly the same for json

# 1
import pandas as pd

df = pd.read_csv("C:\ML journy\python_learn\heart.csv")
print(df)


print("-" * 50)


# 2 - review all the data 
import pandas as pd

df = pd.read_csv("C:\ML journy\python_learn\heart.csv")
print(df.to_string())


print("-" * 50)


# selection 

# 1 - for a column
import pandas as pd

df = pd.read_csv("C:\ML journy\python_learn\heart.csv")
print(df["target"])
print(df[["target", "age"]])



print("-" * 50)


# 2 - by row/s
import pandas as pd

df = pd.read_csv("C:\ML journy\python_learn\heart.csv")
print(df)


print("-" * 50)


import pandas as pd

df = pd.read_csv("C:\ML journy\python_learn\heart.csv", index_col="age")
print(df.iloc[0:10:2, 2:4])


print("-" * 50)


# filtring

# 1 
import pandas as pd
df = pd.read_csv("data.csv")
print(df)


print("-" * 50)


# 2
import pandas as pd
df = pd.read_csv("data.csv")
bb = df[df["Legendary"] == True]
print(bb)

print("-" * 50)

ff = df[(df["Type1"] == "fire") | (df["Type2"] == "Flying")]
print(ff)


print("-" * 50)


# 3
import pandas as pd
df = pd.read_csv("data.csv")
hello = df[(df["Height"] >= 5) |
           (df["Weight"] < 10)]
print(hello)


print("-" * 50)


# aggregation

# 1 - whole df
import pandas as pd
df = pd.read_csv("data.csv")
print(df.mean(numeric_only=True))
print("-" * 50)

print(df.max(numeric_only=True))
print("-" * 50)

print(df.min(numeric_only=True))
print("-" * 50)

print(df.count())
print("-" * 50)


# 2 - for column
print(df["Height"].mean(numeric_only=True))
print("-" * 50)

print(df["Height"].max(numeric_only=True))
print("-" * 50)

print(df["Height"].min(numeric_only=True))
print("-" * 50)

print(df["Height"].count())
print("-" * 50)


# 3 - use groupby() func
group = df.groupby("Type1")
print(group["Height"].mean())
print("-" * 50)

print(df["Height"].sum(numeric_only=True))
print("-" * 50)

print(df["Height"].min(numeric_only=True))
print("-" * 50)

print(df["Height"].count())
print("-" * 50)


# data cleaning

# 1 - drop column

import pandas as pd
df = pd.read_csv("data.csv")
df = df.drop(columns=["No", "Legendary"])
print(df)


print("-" * 50)


# 2 - handle missing data

# if drop it 
#df = df.dropna(subset=["Type2"])
print(df.to_string())


print("-" * 50)

# if fill
df = df.fillna({"Type2": "NONE"})
print(df.to_string())


print("-" * 50)


# 3 - fix inconsestent values 
import pandas as pd
df = pd.read_csv("data.csv")
df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE"})
print(df.to_string())


print("-" * 50)


# 4 - starndaried text
df["Name"] = df["Name"].str.lower()
print(df)


print("-" * 50)


# 5 - fix data type
df["Legendary"] = df["Legendary"].astype(bool)
print(df)


# 6 - remove duplicate
df = df.drop_duplicates()
print(df.to_string())
