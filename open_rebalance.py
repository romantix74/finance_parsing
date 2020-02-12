S=1200
# название и доля
s_portfel= {
"CASH":0.15,
"AFKS":0.10,
"ALRS":0.20,
"OTHER":0.55,
}

# портфель без кэша
R=340

def calc():
  print("R приведенный к S: {}".format( S - S*s_portfel["CASH"]))
  print(s_portfel)
  
  print("S в рубляx \n")
  
  # считаем в рублях
  for k,v in s_portfel.items():
    print("{} = {}".format(k,v*S))
  
  
  print("\nR в рубляx \n")
  # переводим в R
  for k,v in s_portfel.items():
    print("{} = {}".format(k,v*R))
  print("\n")

if __name__ == "__main__":
  # проверка, что сумма равна 100%
  sum = 0
  for k,v in s_portfel.items():
    print(k)
    sum += v  
  if (sum != 1):
    print("не правильные проценты !!!\n")

  calc()
  