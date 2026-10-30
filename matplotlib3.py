# intro
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([50, 60, 70, 80])
# y = np.array([5.5, 16, 7, 20])

# plt.plot(x, y)
# plt.show()

# print('-' * 50)


# plot customaization
# import matplotlib.pyplot as plt
# import numpy as np

# style = dict(marker=".",
#              markersize=4,
#              mfc="#eb34ba",
#              mec="#a8087d",
#              linestyle="-",
#              linewidth=2,
#              )

# x = np.array([2000, 3000, 7000, 8000])
# y1 = np.array([5.5, 16, 7, 20])
# y2 = np.array([10, 30, 15, 20])
# y3 = np.array([36, 46, 29, 50])


# plt.plot(x, y1, color="#e368c2", **style)
# plt.plot(x, y2, color="#ed9ac8", **style)
# plt.plot(x, y3, color="#cf3c77", **style)

# plt.show()


print("-", 50)


# labels 
# import matplotlib.pyplot as plt
# import numpy as np

# style2 = dict(marker="*",
#              markersize=4,
#              mfc="#eb34ba",
#              mec="#a8087d",
#              linestyle="-",
#              linewidth=2
#              )

# x = np.array(["JAN", "FEB", "MAR", "APR", "JUN"])
# y1 = np.array([19, 20, 35, 25, 46])
# y2 = np.array([5, 16, 17, 8, 19])

# plt.title("yearly temprature",
#           fontsize=20, 
#           family="Arial",
#           fontweight="bold")

# plt.xlabel("months",
#            fontsize=15,
#            family="Arial",
#            fontweight="bold",
#            color="#3429ab")

# plt.ylabel("tempreture",
#            fontsize=15,
#            family="Arial",
#            fontweight="bold",
#            color="#3429ab")

# plt.tick_params(axis="both")

# plt.plot(x, y1, color="#5a71f2", **style2)
# plt.plot(x, y2, color="#bf5af2", **style2)

# plt.show()


print("-", 50)


# gridline
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5, 10, 15, 20])
# y = np.array([16, 10, 8, 2])

# plt.grid(axis="both",
#          color="lightgray",
#          linewidth=2,
#          linestyle="solid")

# plt.plot(x, y)
# plt.show()


print("-", 50)


# bar chart
import matplotlib.pyplot as plt
import numpy as np

# veges = ["apple", "carrot", "tomato", "banana"]
# values = np.array([20, 10, 15, 30])

# plt.bar(veges, values, color="#f25ac9")

# plt.title("how much veges a week", color="#236b40", fontweight="bold")
# plt.xlabel("kind", color="#236b40", fontweight="bold")
# plt.ylabel("quantity", color="#236b40", fontweight="bold")

# plt.show()


print("-", 50)

# bie chart
import matplotlib.pyplot as plt
import numpy as np

# years = ["year1", "year2", "year3", "year4"]
# numss = np.array([1000, 950, 900, 700])
# color = ["lightpink", "purple", "pink", "white"]

# plt.pie(numss, labels=years, autopct="%0.1f%%", colors=color, explode=[0,0.1,0,0],shadow=True)

# plt.show()


print("-", 50)


# scatter chart
# 1
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 1, 5 ,2, 3, 6, 7, 4, 9])   # hours study
y1 = np.array([0, 12, 12, 80, 25, 85, 57, 89, 20, 97])     # grades

x2 = np.array([0, 2, 1, 5 ,2, 3, 6, 7, 8, 9])   # hours study
y2 = np.array([0, 20, 12, 80, 30, 90, 60, 92, 21, 99])

plt.title("grade score", fontweight="bold", color="#5735b5")
plt.xlabel("hours study", fontweight="bold", color="#5735b5")
plt.ylabel("grades", fontweight="bold", color="#5735b5")

plt.scatter(x1, y1, alpha=0.5, s= 100, label="class A")
plt.scatter(x2, y2, color="red", alpha=0.5, s= 100, label="class B")

plt.legend()
plt.show()

# 2