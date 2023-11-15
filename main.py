def show_graphic():
    temperature = input.temperature()
    led.plot_bar_graph(temperature, 50)

basic.forever(show_graphic)