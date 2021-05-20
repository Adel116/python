profit = float(input("введите вашу выручку"))
coast = float(input("введите ваши издержки"))
if profit > coast:
    print(f"работаете в плюс")
    workers = int(input("введите число сотрудников"))
    print(f"прибыль на одного {profit / workers}")
elif profit == coast:
  print("работаете в ноль")
else:
      print(" работаете в убыток")