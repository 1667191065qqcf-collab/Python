from matplotlib import pyplot as plt

#grafica circular

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode=[0,0,0,0.1,0] #distancia separado del radio

plt.pie(slices, labels=labels,explode=explode, startangle=90,
        autopct="%1.1f%%", #para mostrar el porcentaje de cada slice
        shadow=True, wedgeprops={"edgecolor":"black"})

plt.style.use("fivethirtyeight")
plt.title("My awesome Pie chart")
plt.show()

