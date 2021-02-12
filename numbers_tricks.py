print("***  Modulus Operator %")
for i in range(3, 6):
    print(f"* {i} % 3 =", i % 3)

print("\n###  Exponentiation Operator **")
for i in range(2, 5):
    print(f"# {i} ** {i} =", i ** i)

print("\n$$$  Floor Division //")
for i in range(9, 20, 4):
    print(f"$ {i} // 5 =", i // 5)


x = 10
x *= 5
print(f"* x was 10, and x *= 5 making x =", x)
y = 22
y //= 4
print(f"* y was 22, and y //= 4 making y =", y)
z = 30
z **= 2
print(f"* z was 30, and z **=2 making z =", z)

x = [1, 2, 3]
x *= 3
print(x)

a = 2.2
b = 1.1
c = a + b
print("The value of c is", c)
print("Is c equal to 3.3?", c == 3.3)

from decimal import Decimal

a_Decimal = Decimal('2.2')
b_Decimal = Decimal('1.1')
c_Decimal = a_Decimal + b_Decimal
print("The value of c_Decimal is", c_Decimal)
print("Is c_Decimal to 3.3?", c_Decimal == 3.3)
print("Is c_Decimal to Decimal('3.3')?", c_Decimal == Decimal('3.3'))

from fractions import Fraction

one_ninth = Fraction(1, 9)
one_seventh = Fraction(1, 7)
ninth_plus_seventh = one_ninth + one_seventh
ninth_multiply_seventh = one_ninth * one_seventh
print("one_ninth's value is:", one_ninth)
print("one_seventh's value is:", one_seventh)
print("addition of the two:", ninth_plus_seventh)
print("multiplication of the two:", ninth_multiply_seventh)

print("*** You can choose whether to normalize the fraction. By default, it's normalized.")
print('Normalize: 3/9 is', Fraction(3, 9, _normalize=True))
print('non-normalized: 3/9 is', Fraction(3, 9, _normalize=False))

print("*** You can access a fraction's numerator and denominator.")
two_seventh = Fraction(2, 7)
print(f"{two_seventh}'s numerator:", two_seventh.numerator)
print(f"{two_seventh}'s denominator:", two_seventh.denominator)

print("*** Convertions between floats and fractions")
print(f"{two_seventh} expressed as floats:", float(two_seventh))
print(f"0.5 expressed as fraction:", Fraction(*0.5.as_integer_ratio()))

large_number = 7323843829343
print("Formatted: {:_d}".format(large_number))
print("Formatted: {:,d}".format(large_number))

scores = [95, 97, 94, 97, 95, 93]
mean_score = sum(scores) / len(scores)
print("Raw Score:", mean_score)
print(f"Formatted: {mean_score:.2f}")
print(f"Formatted from rounding: {round(mean_score, 2)}")

large_number = 2834000000000
small_number = 0.00000003213
print(f"Formatted large number: {large_number:e}")
print(f"Formatted small number: {small_number:e}")

current_apr = 0.03792343
discount_rate = 0.333333
print(f"Current APR: {current_apr:.2%}")
print(f"Discount Rate: {discount_rate:.4%}")

