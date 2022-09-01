class Contacts:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size



    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True


    def get(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


    
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
      #we use the range because the because we are iterating through for the index
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] ==  key:
                self.map[key_hash].pop(i)
                return True



    def print(self):
        print("")
        print("::::::PHONEBOOK DIRECTORY::::::")
        print("")

        for item in self.map:
            if item is not None:
                print(str(item))


C = Contacts()
C.add("salim", "0557553975")
C.add("fahim","4668583945")
C.add("adams","244137006")
C.add("Jawad","3245235326")

C.print()
C.delete("fahim")
C.print()
C.get("salim")
     