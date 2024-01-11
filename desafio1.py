nome = "Thiago"
xp = 5020
if xp <= 1000:
    classe = "Ferro"
elif xp <= 2000:
    classe = "Bronze"
elif xp <= 5000:
    classe = "Prata"
elif xp <= 7000:
    classe = "Ouro"
elif xp <= 8000:
    classe = "Platina"
elif xp <= 9000:
    classe = "Ascendente"
elif xp <= 10000:
    classe = "Imortal"
else:
    classe = "Radiante"

print("O Herói de nome {0} está no nivel de {1}." .format(nome,classe))