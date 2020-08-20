payments = {"client1" : 1000000,"client2" : 500000,"client3" : 250000}
newPayments = payments.values()
totalPayments = sum(newPayments)
VAT = 0.16 * totalPayments
def getInclusive(totalPayments):
    return lambda inclusive : VAT + totalPayments
getInclusive(totalPayments)
inclusive = getInclusive(totalPayments)


print("Ksh{:,.2f}".format(inclusive(VAT)))