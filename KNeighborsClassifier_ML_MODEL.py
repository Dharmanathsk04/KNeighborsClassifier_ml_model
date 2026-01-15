from sklearn.neighbors import KNeighborsClassifier

x = [[1],[2],[3],[6],[7],[8]]


y = [0,0,0,1,1,1]


model = KNeighborsClassifier(n_neighbors=3).fit(x,y)

print(model.predict([[5]]))

