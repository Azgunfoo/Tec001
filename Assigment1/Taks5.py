talent = float(input("Enter talent:"))
pound = float(input("Enter pound:"))
lot = float(input("Enter lots:"))
total_lot = (talent*20*32) + (pound*32) + lot
total_gram = (total_lot*13.3)
total_kg = int((total_gram /1000))
gram = total_gram % 1000
print ("The weight in morden unit is:")
print (f"{total_kg}kilogram and {total_gram:.0f}gram")