def calculate_u(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp
 
def calculate_factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
 
if __name__ == "__main__":
    num_years = 6
    years = [1941, 1951, 1961, 1971, 1981, 1991]
 
    population = [[0 for _ in range(num_years)] for _ in range(num_years)]
    population[0][0] = 12
    population[1][0] = 15
    population[2][0] = 20
    population[3][0] = 27
    population[4][0] = 39
    population[5][0] = 52
 
    for i in range(1, num_years):
        for j in range(num_years - 1, i - 1, -1):
            population[j][i] = population[j][i - 1] - population[j - 1][i - 1]
 
    year_1976 = 1976
    year_1978 = 1978
 
    population_1976 = population[num_years - 1][0]
    u_1976 = (year_1976 - years[num_years - 1]) / (years[1] - years[0])
    for i in range(1, num_years):
        population_1976 += (calculate_u(u_1976, i) * population[num_years - 1][i]) / calculate_factorial(i)
 
    population_1978 = population[num_years - 1][0]
    u_1978 = (year_1978 - years[num_years - 1]) / (years[1] - years[0])
    for i in range(1, num_years):
        population_1978 += (calculate_u(u_1978, i) * population[num_years - 1][i]) / calculate_factorial(i)
 
    population_increase = population_1978 - population_1976
    print("Population in 1976:", population_1976)
    print("Population in 1978:", population_1978)
    print("Increase in population from 1976 to 1978:", population_increase)