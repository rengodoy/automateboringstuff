market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersections):
    for key in intersections.keys():
        if intersections[key] == 'green':
            intersections[key] = 'yellow'
        elif intersections[key] == 'yellow':
            intersections[key] = 'red'
        elif intersections[key] == 'red':
            intersections[key] = 'green'
    assert 'red' in intersections.values(), 'Neither light is red!' + str(intersections)
 

switchLights(market_2nd)