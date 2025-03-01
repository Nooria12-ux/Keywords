def due(b,g):
    return g-b
bill = int(input("Yoi, enter the Bill amount: "))
given = int(input("And the given amount broski: "))

dueAmount = due(bill, given)

print(f"Due Amount: {dueAmount}")