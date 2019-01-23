from random import choice, randint
from math import sqrt
from copy import deepcopy

perfectSquares = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729,784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444,1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500)
# A trinomial is factorable if b^2 - 4ac is a perfect square.

def getSimpleCoeffs():
    while True:
        a = choice((-1, 1))
        b = randint(-52, 52)
        c = randint(-52, 52)

        if b ** 2 - 4*a*c in perfectSquares and 0 not in (b, c) and b - c not in (-1, 1, -2*b):
            break
    
    coeffs = list(map(str, [a, b, c]))

    return coeffs
# Gets the coefficients of the trinomial.
    

def getTrickyCoeffs():
    while True:
        a = randint(1, 25)
        b = randint(-25, 25)
        c = randint(-25, 25)

        if b ** 2 - 4*a*c in perfectSquares and 0 not in (a, b, c) and a != 1:
            break
    
    coeffs = list(map(str, [a, b, c]))

    return coeffs
# Gets the coefficients of the trinomial.


def getSimpleTrinomial(coeffsList):
    coeffs = coeffsList.copy()
    if int(coeffs[0]) > 0:
        coeffs[0] = ""
    else:
        coeffs[0] = "-"

    for i in range(1, len(coeffsList)):
        if int(coeffs[i]) > 0:
            coeffs[i] = " + " + coeffs[i]
        elif int(coeffs[i]) < 0:
            coeffs[i] = " - " + coeffs[i].strip("-")

    return coeffs[0] + "x^2" + coeffs[1] + "x" + coeffs[2]
# Takes coefficients and creates the trinomial as a string.


def getTrickyTrinomial(coeffsList):
    coeffs = coeffsList.copy()
    for i in range(1, len(coeffs)):
        if int(coeffs[i]) > 0:
            coeffs[i] = " + " + coeffs[i]
        elif int(coeffs[i]) < 0:
            coeffs[i] = " - " + coeffs[i].strip("-")
    
    return coeffs[0] + "x^2" + coeffs[1] + "x" + coeffs[2]
# Takes coefficients and creates the trinomial as a string.


def factorSimple(coeffs):
    coeffs = list(map(int, coeffs.copy()))
    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]

    if a < 0:
        negativeSign = "-"
    else:
        negativeSign = ""

    root1 = -int((-b + sqrt(b ** 2 - 4*a*c)) / 2*a)
    root2 = -int((-b - sqrt(b ** 2 - 4*a*c)) / 2*a)

    if root1 > 0:
        root1 = " + " + str(root1)
    else:
        root1 = " - " + str(root1).strip("-")
    
    if root2 > 0:
        root2 = " + " + str(root2)
    else:
        root2 = " - " + str(root2).strip("-")
    
    return negativeSign + "(x" + root1 + ")(x" + root2 + ")"
# Uses the quadratic formula to get the roots of simple trinomials.

def getFactors(n):
    factors = []
    for i in range(1, abs(n )+ 1):
        if n % i == 0:
            factors.append(i)
    
    return factors


def getGCF(a, b, c):
    factorsA = getFactors(a)
    factorsB = getFactors(b)
    factorsC = getFactors(c)

    commonFactors = []

    for i in factorsA:
        for j in factorsB:
            for k in factorsC:
                if i == j and j == k:
                    commonFactors.append(i)
    
    if len(commonFactors) < 1:
        commonFactors.append(1)
    
    return max(commonFactors)


def commonFactor(coeffsList):
    coeffs = coeffsList.copy()
    gcf = getGCF(*coeffs)

    for i in range(len(coeffs)):
        coeffs[i] //= gcf
    
    return (coeffs, gcf)


#######################################################################
# Factoring Tricky Trinomials (ax^2 + bx + c where a != -1, 1 or 0)

def getFactorPairs(n):
    posFactorPairs1 = []

    if n > 0:
        for i in range(1, n + 1):
            if (n / i) % int(n / i) == 0:
                posFactorPairs1.append([i, n // i])

        posFactorPairs2 = deepcopy(posFactorPairs1)
        
        for i in range(len(posFactorPairs2)):
            posFactorPairs2[i][0] = -posFactorPairs2[i][0]
            posFactorPairs2[i][1] = -posFactorPairs2[i][1]

        factorPairs = posFactorPairs1 + posFactorPairs2
    else:
        for i in list(range(n, 0)) + list(range(1, -n + 1)):
            if (n / i) % int(n / i) == 0:
                posFactorPairs1.append([i, n // i])
            
            factorPairs = posFactorPairs1

    return factorPairs
# Gets the factor pairs of n; Order matters.


def factorTricky(coeffsList):
    coeffs = coeffsList.copy()

    commonFactorCall = commonFactor(coeffs)

    factoredOut = commonFactorCall[1]
    coeffs = commonFactorCall[0]

    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]

    factorsA = getFactorPairs(a)
    factorsB = getFactorPairs(c)
    out = [factoredOut]
    breakCondition = False

    for i in factorsA:
        for j in factorsB:
            if i[0] * j[1] + i[1] * j[0] == b:
                out.append([i[0], j[0]])
                out.append([i[1], j[1]])
                
                breakCondition = True
                break
            
        if breakCondition == True:
            break

    # Formatting
    if out[1][0] == 1:
        out[1][0] = "x"
    else:
        out[1][0] = str(out[1][0]) + "x"
    out[2][0] = str(out[2][0]) + "x"

    if out[0] == 1:
        out[0] = ""
    else:
        out[0] = str(out[0])

    for i in range(1, len(out)):
        out[i] = list(map(str, out[i]))

    for i in range(1, 3):
        if int(out[i][1]) < 0:
            out[i][1] = out[i][1].strip("-")
            out[i][1] = " - " + out[i][1]
        else:
            out[i][1] = " + " + out[i][1]

    factoredTrinomial = out[0] + "(" + out[1][0] + out[1][1] + ")(" + out[2][0] + out[2][1] + ")"

    return factoredTrinomial
