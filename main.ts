basic.forever(function show_graphic() {
    let temperature = input.temperature()
    led.plotBarGraph(temperature, 50)
})
