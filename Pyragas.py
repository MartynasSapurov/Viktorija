kg_kaina = 7.55
perkame_gramu = 700
pyrago_kg_kaina = float(input("Įveskite pyrago kainą\n"))
pyrago_svoris = float(input("Įveskite pyrago svorį\n"))

salainiu_kaina = kg_kaina * 700/1000
pyrago_kaina = pyrago_kg_kaina * pyrago_svoris
pirkinio_kaina = salainiu_kaina + pyrago_kaina

print(f"Saldainių kaina: {salainiu_kaina} Eur")
print(f"Pyrago kaina: {pyrago_kaina} Eur")
print(f"Pirkinio kaina: {pirkinio_kaina} Eur")
