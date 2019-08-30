# tupla com os times do campeonato brasileiro
# - os 5 primeiros colocados , - os 4 ultimos , - ordem alfabetica (sorted),
# tupla.index(chapecoense);

brasileirao20019 = (" Flamengo"," Santos"," Palmeiras"," São Paulo",
                    " Corinthians"," Atlético-MG"," Internacional"," Bahia",
                    " Botafogo"," Athletico-PR"," Goiás"," Grêmio",
                    " Ceará"," Vasco da Gama"," Fortaleza"," Cruzeiro",
                    " Chapecoense"," Fluminense"," CSA", " Avaí")
print("Os cinco primeiros colocados são: ")
for primeiros in range (0, 5):
    print(f">>{primeiros+1}o. : {brasileirao20019[primeiros]}")

print("\nOs quatro últimos colocados são: ")
for ultimos in range(16, len(brasileirao20019)):
    print(f">>{ultimos+1}o.: {brasileirao20019[ultimos]}")
print("\nOs times em ordem alfabetica são: ")
print(sorted(brasileirao20019))
chape = brasileirao20019.index(" Chapecoense")
print("\nA Chapecoense está na posição :", chape + 1 )