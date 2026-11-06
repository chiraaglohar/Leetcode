
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        products = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                d1 = int(num1[i])
                d2 = int(num2[j])
                products[i + j + 1] += d1 * d2

        carry = 0
        for i in range(len(products) - 1, -1, -1):
            total = products[i] + carry
            products[i] = total % 10
            carry = total // 10

        result = ''.join(map(str, products)).lstrip('0')
        return result if result else "0"