from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("lineR1A1.html")

p = figure(plot_width=800, plot_height=800)

# add a circle renderer with a size, color, and alpha
#p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

p.circle([752841.9805521033,768795.3520995112,753975.2964454206], [202009.7969697361,190154.05272175817,205090.10627287443], size=20, color="red", alpha=0.5)

# show the results
show(p)


