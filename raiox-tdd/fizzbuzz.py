"""
Regras do FizzBuzz:

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição: posição

Metodologia do TDD:
- sempre tentar resolver o teste da forma mais simples, mesmo que ela não seja
a melhor de todas.
- 3 assert's == fazer refatoração
"""
from functools import partial

multiple_of = lambda base, num: num % base == 0
# def multiple_of(base, num):
#     return num % base == 0

multiple_of_three = partial(multiple_of, 3)
# def multiple_of_three(num):
#     return multiple_of(3, num)

multiple_of_five = partial(multiple_of, 5)
# def multiple_of_five(num):
#     return multiple_of(5, num)

def robot(pos):
    say = str(pos)

    if multiple_of_three(pos) and multiple_of_five(pos):
        say = "fizzbuzz"
    elif multiple_of_three(pos):
        say = "fizz"
    elif multiple_of_five(pos):
        say = "buzz"

    return say

"""
- Nosso próprio testador:

def assert_equal(result, expected):
    from sys import _getframe

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno

        print(f"Fail: Line {line_no} got {result} expecting {expected}")

if __name__ == "__main__":
    assert_equal(robot(1), "1")
    assert_equal(robot(2), "2")
    assert_equal(robot(4), "4")

    assert_equal(robot(3), "fizz")
    assert_equal(robot(6), "fizz")
    assert_equal(robot(9), "fizz")

    assert_equal(robot(5), "buzz")
    assert_equal(robot(10), "buzz")
    assert_equal(robot(20), "buzz")

    assert_equal(robot(15), "fizzbuzz")
    assert_equal(robot(30), "fizzbuzz")
    assert_equal(robot(45), "fizzbuzz")
"""
