def fibonachi():
    res = []
    """
    Fibonachi list
    """
    def fib_1(n):
        """
        Fill the Fibonachi list
        :param n: number of elements
        :return: Fibonachi list
        """
        if not isinstance(n, int):
            raise TypeError('must be int')
        if len(res) > n:
            return res[:n]
        if len(res) != 0:
            first_number = res[len(res)-2]
            second_number = res[len(res)-1]
        else:
            first_number = 0
            second_number = 1
        for i in range(len(res), n):
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number
            res.append(next_number)
        return res
    return fib_1


if __name__ == "__main__":
    try:
        f = fibonachi()
        print(f(4))
        print(f(10))
        print(f(4))
        print(f(2))
    except Exception as err:
        print(err)
