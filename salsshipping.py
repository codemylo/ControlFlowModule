weight = 4.8
cost_ground = 0

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Standard Ground Shipping will cost:", cost_ground)

#Ground Premium Shipping
cost_ground_premium = 125

print("Ground Shipping Premium is:", cost_ground_premium)


#Drone Shipping
cost_drone = 0

if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping will cost:", cost_drone)



