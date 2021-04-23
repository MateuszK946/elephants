import fileinput
data = []
for line in fileinput.input(): # metoda słóżąca do wpisywania danych w terminalu poprzez: python slonie.py "slo1ocen.in"
    data.append(line.rstrip()) # plik z programem powinien znajdować się w tym samym folderze co program

numbre_of_elephants = int(data[0]) # ilość sloni
weight_of_elephants = [int(x) for x in data[1].split()] # wagi słoni
current_positions = [int(x) for x in data[2].split()] # obecna pozycje słoni
expected_positions = [int(x) for x in data[3].split()] # pozycje finalne słoni
suma = 0 # zmienna, do której będzie zapisywana suma wag słoni
positions = current_positions.copy() # kopia listy obecnych pozycji słoni, na której bedą wykonywane operacje
weight = weight_of_elephants.copy() # kopia wagi słoni
copy_of_sorted_weight = sorted(weight).copy() # posortowana waga słoni od najmniejszej do największej
c = 0

while True: # pętla programu
    if positions == expected_positions: # warunek wyjścia z pętli
        break
    elif positions != expected_positions:
        if copy_of_sorted_weight == []: # jeśli po wykonaniu programu okazałoby się że jakieś słonie nie zostały przyporządkowane
            for i in range(numbre_of_elephants):
                if positions[i] != expected_positions[i]:
                    suma += weight_of_elephants[positions[i]-1] + weight_of_elephants[expected_positions[i]-1]
                    positions[positions.index(expected_positions[i])] = positions[i]
                    positions[i] = expected_positions[i]
        else: # wyszukiwany jest słoń o najmniejszej wadze i zamieniany ze słoniem, który powinien stać na jego miejscu
            slon_weight_min = copy_of_sorted_weight[c]
            numer_slonia = weight.index(slon_weight_min)
            slon_1_nr = numer_slonia + 1
            slon_1_pos = positions.index(slon_1_nr)
            slon_2_nr = expected_positions[slon_1_pos]
            slon_2_pos = positions.index(slon_2_nr)
            if slon_1_pos != slon_2_pos:
                positions[slon_1_pos] = slon_2_nr
                positions[slon_2_pos] = slon_1_nr
                suma += weight_of_elephants[slon_1_nr - 1] + weight_of_elephants[slon_2_nr - 1]
            else:
                del copy_of_sorted_weight[c]
                weight_of_elephants[slon_1_nr - 1] = 0

print(suma)
