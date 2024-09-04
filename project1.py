from matplotlib import pyplot as plt
# x = [1,2,3,4,5,6,7,8,9]
# y = [1, 4, 7, 1, 9, 3, 5, 1, 9]
# x2 = [1,2,3,4,5,6,7,8,9]
# y2 = [9, 1, 5, 3, 9, 3, 1, 8, 4]
# plt.plot(x,y, 'r')
# plt.plot(x2,y2, 'g')
# plt.plot(x,y, 'ro')
# plt.plot(x2,y2, 'go')

# plt.title("Graph")
# plt.xlabel("Order")
# plt.ylabel("COunt")
# plt.show()

# plt.bar(x,y,color='b', label='profit')
# plt.bar(x2,y2,color='g', label='Tax')

# plt.legend()
# plt.title("Graph")
# plt.xlabel("Order")
# plt.ylabel("Count")
# plt.show()

# age = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.hist(age, range)
# plt.title("Graph")
# plt.xlabel("Order")
# plt.ylabel("Count")
# plt.grid()
# plt.show()

# plt.scatter(x,y, marker='*', color= 'r')
# plt.title("Graph")
# plt.xlabel("Order")
# plt.ylabel("Count")
# plt.show()



x = [1,2,3,4,5,6,7,8,9]
y = [1, 4, 7, 1, 9, 3, 5, 1, 9]
x2 = [1,2,3,4,5,6,7,8,9]
y2 = [9, 1, 5, 3, 9, 3, 1, 8, 4]

plt.subplot(2, 1, 1)
plt.title("Subplot 1")
plt.plot(x, y, 'r')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'g')
plt.show()
