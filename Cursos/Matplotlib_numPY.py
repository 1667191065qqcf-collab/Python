from matplotlib import pyplot as plt

#Es literalmente lo que hacemos en matlab pero en python

#print(plt.style.available)
plt.style.use("Solarize_Light2")


valor_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]


valor_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

plt.plot(valor_x, valor_y, color="k",linestyle="--", marker="",label="Todos los desarrolladores")

valor_y_2 = [45372, 23232, 34564, 94873, 18276, 35456, 17827, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

plt.plot(valor_x, valor_y_2, "b" ,marker ="o", label ="Python")

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]


plt.plot(valor_x, js_dev_y, "r" , linewidth =2, label ="javascript")

plt.title("Salario medio")
plt.xlabel("Años")
plt.ylabel("Salario")

plt.legend()
#plt.legend(["todos los desarrolladores","Python"]) otra forma de implementar la leyenda

plt.grid(True)
plt.tight_layout()

plt.savefig("plot.png")

plt.show()

#formato de linea -> al manual




