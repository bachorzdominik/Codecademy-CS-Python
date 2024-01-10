'''
Platform:    codecademy.com
Career Path: Computer Science
Project:     The Boredless Tourist
'''

test_traveler1 = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
test_traveler2 = ['Dereck Smill', 'Paris, France', ['monument']]
destinations   = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
attractions    = [[] for x in destinations]


def get_destination_index(destination):
    destination_index = destinations.index(destination)

    return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index


def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)

    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  
    return attractions_for_destination
  

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
      attraction_tags = possible_attraction[1]
      for interest in interests:
        if interest in attraction_tags:
          attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


def get_attractions_for_traveler(traveler):
    traveler_destination  = traveler[1]
    traveler_interests    = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler[1]}: {', '.join([x for x in traveler_attractions])}"

    return interests_string


add_attraction("Los Angeles, USA",  ['Venice Beach', ['beach']])
add_attraction("Paris, France",     ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France",     ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China",   ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China",   ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China",   ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA",  ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt",      ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt",      ["Egyptian Museum", ["museum"]])


smills_france = get_attractions_for_traveler(test_traveler2)
print(smills_france)
