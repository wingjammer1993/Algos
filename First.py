class MapSum:
    def __init__(self):
        self.map_sum_dict = {}
        self.value = 0
        
    def insert(self, key, val):
        self.map_sum_dict[key] = val

    def sum(self, prefix):
        map_sum = 0
        for keys in self.map_sum_dict:
            if keys.startswith(prefix):
                value = self.map_sum_dict.get(keys)
                map_sum = map_sum + value
        return map_sum


'''if __name__ == "__main__":

    obj = MapSum()
    obj.insert("apple", 3)
    obj.insert("app", 2)
    param_2 = obj.sum("app")
    print(param_2)'''
