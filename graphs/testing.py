import pygal
bar_chart = pygal.Bar()
bar_chart.add("Fib", [0, 1, 1, 2, 3, 5, 8])
bar_chart.render_to_file("testing.svg")
