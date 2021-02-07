"""
Regras do Happy number

1. Dado um número inteiro positivo
2. Substitua o número pela soma dos quadrados dos seus dígitos.
3. Se o resultado for 1, o número é feliz
4. Caso contrário, repita o processo indefinidamente.

Exemplo:
- número: 7
7ˆ2 = 49
4ˆ2 + 9ˆ2 = 16 + 81 = 97
9ˆ2 + 7ˆ2 = 81 + 49 = 130
1ˆ2 + 3ˆ2 + 0ˆ2 = 1 + 9 + 0 = 10
1ˆ2 + 0ˆ2 = 1
return happy

- Se o número chegar nele mesmo, é:
return not happy

## Primeira versão estável
def sum_of_digits(num):
    string = str(num)

    digits = [int(char) ** 2 for char in string]

    return sum(digits)

def happy(num):
    if num in (1, 10, 100, 97, 130):
        n = num
        while n != 1:
            n = sum_of_digits(n)
        return n == 1

    return False
"""

# Resultado final
def happy(num):
    next_ = sum(int(char) ** 2 for char in str(num))
    return num in (1, 7) if num < 10 else happy(next_)

## Primeira versão estável
# assert sum_of_digits(130) == 10
assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
