times=('Flamengo','Santos','Palmeiras','Grêmio','Athletico','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco','Atlético-MG','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')

print(f'Os 5 primeiros colocados são {times[0:5]} ')
print(f'Os 4 ultimos colocados são {times[-4:]} ')
print(f'Os times na ordem alfabetica são {sorted(times)} ')
print(f'O Chape ta na posição  {times.index("Chapecoense")+1}'  )