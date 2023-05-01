import matplotlib.pyplot as plt

#initialize array of weights
with open("data8.csv", "r") as f:
    lines = f.read().split()
weights_array = lines #initial array of weights
new_array = [float(i) for i in weights_array] #new array to hold distribution of weights

#calculating mean weight
mean_weight = sum(new_array)/len(new_array)
#calculating X
below_8 = 0.33*len([x for x in new_array if (x<8)])
#plotting histogram
plt.hist(new_array, label="Distribution of weights among newborns")
plt.title("Histogram of weight distribution in Europe")
plt.xlabel("Weights (Kg)")
plt.ylabel("Frequency")
plt.annotate("Mean weight: " +str(mean_weight), xy=(2.5,100))
plt.annotate("Number of weights below 8Kg: " + str(below_8), xy=(2.5, 90))
plt.legend(loc="center right")
plt.show();