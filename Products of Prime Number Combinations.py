def primeProducts(primes):
    result = []

    def dfs(index, product):
        if index == len(primes):
            if product != 1:
                result.append(product)
            return

        # Don't include current prime
        dfs(index + 1, product)

        # Include current prime
        dfs(index + 1, product * primes[index])

    dfs(0, 1)
    return result