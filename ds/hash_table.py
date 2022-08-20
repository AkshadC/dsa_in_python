class HashTableImplementation:
    def __init__(self, MAX):
        self.MAX = MAX
        self.arr = [[] for i in range(self.MAX)]

    def hash_function(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        hash_value = self.hash_function(key)
        found = False
        for index, element in enumerate(self.arr[hash_value]):
            print(index,"    ", element
                  )
        for index, element in enumerate(self.arr[hash_value]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_value][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash_value].append((key, value))

    def __getitem__(self, key):
        hash_value = self.hash_function(key)
        for element in self.arr[hash_value]:
            if element[0] == key:
                return element[1]


if __name__ == "__main__":
    ht = HashTableImplementation(100)
    ht["march 6"] = 120
    ht["march 6"] = 78
    ht["march 8"] = 67
    ht["march 9"] = 4
    ht["march 17"] = 459
    print(ht["march 17"])
