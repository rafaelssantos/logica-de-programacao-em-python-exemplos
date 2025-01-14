time_A = set(input("Informe os jogadores do time A: ").split(sep=","))
time_B = set(input("Informe os jogadores do time B: ").split(sep=","))
time_C = set(input("Informe os jogadores do time C: ").split(sep=","))
time_D = set(input("Informe os jogadores do time D: ").split(sep=","))

jogadores_inscritos = time_A | time_B | time_C | time_D
# Ou
jogadores_inscritos = time_A.union(time_B).union(time_C).union(time_D)

print("Jogadores inscritos no campeonato:", jogadores_inscritos)