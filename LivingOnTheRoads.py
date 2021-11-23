'''
In a kingdom far, far away, there lives a King Byteasar IX. The history of the kingdom is rich with events and conflicts, most of which is focused on its cities. King Byteasar doesn't want to go down in history as a lame duck ruler, and especially doesn't want to have anything to do with the infamous cities of the kingdom.

Instead, king Byteasar wants to focus on the roads, which is why he issued a new decree: from now on, all roads are to be considered cities, and all cities are to be considered roads. Now his most grateful subjects must pack up their belongings and move out from the cities to the roads, and the cartographers are busy with building a new roadRegister of the kingdom. All roads of the kingdom are to be named for the cities they connect (i.e. [city1, city2], city1 < city2), sorted lexicographically and enumerated starting from 0. A new road register for such a system needs to be created.

Your task is to help the cartographers build the new road register. Handle the challenge, and the glorious kingdom of Byteasar IX will never have to deal with its pesky cities ever again!

Example

For

roadRegister = [
  [false, true,  true,  false, false, false],
  [true,  false, false, true,  false, false],
  [true,  false, false, false, false, false],
  [false, true,  false, false, false, false],
  [false, false, false, false, false, true ],
  [false, false, false, false, true,  false]
]
the output should be

solution(roadRegister) = [
  [false, true,  true,  false],
  [true,  false, false, false],
  [true,  false, false, false],
  [false, false, false, false]
]
'''
def solution(roadRegister):
    roadCity = {}
    roadCityList = []
    roadCityCount = 0
    for i,j in enumerate(roadRegister):
        for k,bol in enumerate(j):
            if i < k and bol == True:
                roadCity[roadCityCount] = [i,k]
                roadCityCount+=1
    output = [[False for x in range(len(roadCity))] for y in range(len(roadCity))] 
    for i,j in roadCity.items():
        for k in range(i,len(roadCity)):
            if i == k:
                continue
            elif j[0] in roadCity[k] or j[1] in roadCity[k]:
                print(str(i)+" "+str(k))
                output[i][k] = True
                output[k][i] = True
    return output