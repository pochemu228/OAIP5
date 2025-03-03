def groundhog_day(strings):
    for i in range(1, len(strings)):
        
        differences = []

        for j in range(len(strings[i])):

            if strings[i][j] != strings[i-1][j]:

                differences.append(j)

        if len(differences) > 2:
            return i, *differences

    return 0, 0


print(groundhog_day(["February 2 Groundhog Day", "february 2 Groundhog Day", "February 2 Groundhog Day"]))
print(groundhog_day(["Groundhog Festival in Punxsutawney", "Groundhog Festival in Punksutawney", "Groundhog Festivel in Punxsutowney"]))
