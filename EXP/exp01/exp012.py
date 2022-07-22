class mylist(list):
    def product(self):
        res = 1
        for item in self:
            res = res * item
        return res


a = mylist([1, 2, 3, 4])
print(a.product())