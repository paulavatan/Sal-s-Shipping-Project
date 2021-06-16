flat_charge = 20


def ground_cost(weight):
    if weight <= 2.00:
        return flat_charge + weight * 1.50
    elif weight > 2.00 and weight <= 6.00:
        return flat_charge + weight * 3.00
    elif weight > 6.00 and weight <= 10.00:
        return flat_charge + weight * 4.00
    else:
        return flat_charge + weight * 4.75


ground_cost(8.4)
print(ground_cost(8.4))

premium_ground_charge = 125


def drone_shipping(weight):
    if weight <= 2.00:
        return weight * 4.50
    elif weight > 2.00 and weight <= 6.00:
        return weight * 9.00
    elif weight > 6.00 and weight <= 10.00:
        return weight * 12.00
    else:
        return weight * 14.25


drone_shipping(1.5)
print(drone_shipping(1.5))


def cheapest_shipping(weight):
    if drone_shipping(weight) < ground_cost(weight):
        return "You should ship using drone shipping. It will cost you " + str(drone_shipping(weight)) + " $."
    elif ground_cost(weight) < premium_ground_charge:
        return "You should ship using  ground shipping. It will cost you " + str(ground_cost(weight)) + " $."
    else:
        return "You should ship using premium ground shipping. It will cost you " + str(premium_ground_charge) + " $."


cheapest_shipping(4.8)
print(cheapest_shipping(4.8))
cheapest_shipping(41.5)
print(cheapest_shipping(41.5))