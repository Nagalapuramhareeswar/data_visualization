# importing pygal
import pygal
import numpy
# creating the chart object
bar_chart = pygal.Bar()
# naming the title
bar_chart.title = 'Bar Chart'	
# Random data
bar_chart.add('A', numpy.random.rand(10))
bar_chart.add('B', numpy.random.rand(10))
bar_chart.add('C', numpy.random.rand(10))
bar_chart.add('D', numpy.random.rand(10))
bar_chart
