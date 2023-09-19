import ita

data = [[ i/100 for i in range(100)] for j in range(150)]
ita.plot.image_show(data)

data = [[[i/100, (i+j)/200, abs(j-i)/100] for i in range(100)]
        for j in range(100)]
ita.plot.image_show(data)

data = [[[(k+i)/30 for i in range(10)] for j in range(10)] for k in range(20)]
ita.plot.animation_show(data)

data = [[[[i/10,j/10,k/20] for i in range(10)] for j in range(10)] for k in range(20)]
ita.plot.animation_show(data, interval=20)

data = [(i - 50) ** 2 for i in range(100)]
ita.plot.plotdata(data)
ita.plot.plotdata(data, line=True)

data = [[(i ** 2 - 500) ** 2, i**2] for i in range(100)]
ita.plot.plotdata(data)
ita.plot.plotdata(data, line=True)

data = [[[i * 10, i * 10] for i in range(10)],
        [[(i * 10 + 25) % 100 , i * 10] for i in range(10)],
        [[(i * 10 + 50) % 100 , i * 10] for i in range(10)],
        [[(i * 10 + 75) % 100 , i * 10] for i in range(10)]]
ita.plot.plotdata(data, line=True)
ita.plot.plot_clusters(data)

import random as rnd
data = [(i * 0.5 + 100 * rnd.random() ,i / 10) for i in range(1000)]
ita.plot.linear_fit(data)

