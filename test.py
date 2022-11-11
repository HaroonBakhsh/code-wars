def nb_year(p0, percent, aug, p):
    years = 0
    current_pop = p0

    return current_pop + current_pop * (percent/100) + aug


print(nb_year(1500, 5, 100, 5000))
