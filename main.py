from functions import *

simpleN = int(input("Please enter the number of simple trinomials you want... (ax^2 + bx + c, a = {-1, 1})\n"))
trickyN = int(input("Please enter the number of tricky trinomials you want... (ax^2 + bx + c, a != {-1, 1}) \n"))
print()
print()

print("SIMPLE TRINOMIALS (" + str(simpleN) + ")")
print("##################################")

for _ in range(simpleN):
    coeffs = getSimpleCoeffs()
    trinomial = getSimpleTrinomial(coeffs)
    ans = factorSimple(coeffs)

    print("Trinomial:", trinomial)
    input("Press <Enter> to see the answer...")
    print()
    print("Ans:", ans)
    input()
    print()
print()
print()

print("TRICKY TRINOMIALS (" + str(trickyN) + ")")
print("##################################")

for _ in range(trickyN):
    coeffs = getTrickyCoeffs()
    trinomial = getTrickyTrinomial(coeffs)
    ans = factorTricky(list(map(int, coeffs)))
    
    print("Trinomial:", trinomial)
    input("Press <Enter> to see the answer...")
    print()
    print("Ans:", ans)
    input()
    print()
