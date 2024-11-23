from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing

        Params:
            "chaining": params = (z, table_size)
            "linear": params = (z, table_size)
            "double": params = (z1, z2, c2, table_size)
        '''
        self.collision_type=collision_type
        self.params=params
        self.size=0
        if collision_type == "Chain":
            self.z = params[0]
            self.table_size = params[1]
            self.table = [[] for _ in range(self.table_size)]
        elif collision_type == "Linear":
            self.z = params[0]
            self.table_size = params[1]
            self.table = [None for _ in range(self.table_size)]
        elif collision_type == "Double":
            self.z1 = params[0]
            self.z2 = params[1]
            self.c2 = params[2]
            self.table_size = params[3]
            self.table = [None for _ in range(self.table_size)]
    
    def letter_to_number(self, alphabet):
        if 'a' <= alphabet <= 'z':
            return ord(alphabet) - ord('a')
        elif 'A' <= alphabet <= 'Z':
            return ord(alphabet) - ord('A') + 26
        else:
            raise ValueError("Invalid character. Only alphabetic characters are allowed.")


    def hash_function(self, key):
        if(self.collision_type=="Double"):
            hash_value = 0
            n = len(key)
            hash_value=self.letter_to_number(key[n-1])
            for i in range(n-2, -1, -1):
                letter_value = self.letter_to_number(key[i])
                hash_value = (hash_value * self.z1 + letter_value) % self.table_size
            return hash_value
        else:
            hash_value = 0
            n = len(key)
            hash_value=self.letter_to_number(key[n-1])
            for i in range(n-2, -1, -1):
                letter_value = self.letter_to_number(key[i])
                hash_value = (hash_value * self.z + letter_value) % self.table_size
            return hash_value
    
    def double_hashing(self, key):
        hash_value = 0
        n = len(key)
        hash_value=self.letter_to_number(key[n-1])
        for i in range(n-2, -1, -1):
            letter_value = self.letter_to_number(key[i])
            hash_value = (hash_value * self.z2 + letter_value) % self.c2
        return self.c2-hash_value
    
    def insert(self, x):
        
        #in probing type, if hash table full, raise Exception(“Table is full”).
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        pass
    
    def get_load(self):
        return self.size/self.table_size
    
    def __str__(self):
        pass
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, key):
        #problem
        #Time complexity is O(|key| + table_size)
        #problem
        slot=self.hash_function(key)
        if self.collision_type == "Chain":
            self.table[slot].append(key)

        elif self.collision_type == "Linear":
            while self.table[slot] is not None:
                slot = (slot+1)%self.table_size
                if(slot==self.hash_function(key)):
                    raise Exception("Table is full")
            self.table[slot] = key

        elif self.collision_type == "Double":
            double_slot=self.double_hashing(key)
            probes = 0
            while self.table[slot] is not None:
                slot = (slot + double_slot) % self.table_size
                probes += 1
                if probes >= self.table_size:  # We've checked every slot
                    raise Exception("Table is full")
            self.table[slot] = key

        self.size+=1
        # print(self.get_load())
    
    def find(self, key):
        slot=self.hash_function(key)
        #problem
        #Time complexity is O(|key| + table_size)
        #problem
        if self.collision_type == "Chain":
            if key in self.table[slot]:
                return True
            else:
                return False
        elif self.collision_type == "Linear":
            initial_slot = slot
            while self.table[slot] is not None:
                if self.table[slot] == key:
                    return True
                slot = (slot + 1) % self.table_size
                if slot == initial_slot:
                    return False
            return False

        elif self.collision_type == "Double":
            initial_slot = slot
            step_size = self.double_hashing(key)
            probes = 0
            while self.table[slot] is not None:
                if self.table[slot] == key:
                    return True
                slot = (slot + step_size) % self.table_size
                probes += 1
                if probes >= self.table_size:  # We've checked every slot
                    return False
            return False
    
    def get_slot(self, key):
        #problem of time complexity and return false
        slot=self.hash_function(key)
        if self.collision_type == "Chain":
            if key in self.table[slot]:
                return slot
            else:
                return False
        elif self.collision_type == "Linear":
            initial_slot = slot
            while self.table[slot] is not None:
                if self.table[slot] == key:
                    return slot
                slot = (slot + 1) % self.table_size
                if slot == initial_slot:
                    return False
            return False

        elif self.collision_type == "Double":
            initial_slot = slot
            step_size = self.double_hashing(key)
            probes = 0
            while self.table[slot] is not None:
                if self.table[slot] == key:
                    return slot
                slot = (slot + step_size) % self.table_size
                probes += 1
                if probes >= self.table_size:  # We've checked every slot
                    return False
            return False
    
    def get_load(self):
        return self.size/self.table_size
    
    def __str__(self):
        if self.collision_type=="Chain":
            ans=""
            for i in range(self.table_size):
                if(self.table[i]!=[]):
                    for j in self.table[i]:
                        ans=ans+j
                        ans=ans+' ; '
                    ans=ans[:-3]
                    ans=ans+' | '
                else:
                    ans=ans+"<EMPTY> | "
            return ans[:-3]
        
        else:  # For Linear and Double
            ans = ""
            for i in range(self.table_size):
                if self.table[i] is not None:
                    ans += self.table[i] + ' | '
                else:
                    ans += "<EMPTY> | "
            return ans[:-3]
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    
    def insert(self, x):
        # x = (key, value)
        # print(type(x[0]))
        slot=self.hash_function(x[0])
        
        if self.collision_type == "Chain":
            self.table[slot].append(x)

        elif self.collision_type == "Linear":
            while self.table[slot] is not None:
                slot = (slot+1)%self.table_size
                if(slot==self.hash_function(x[0])):
                    raise Exception("Table is full")
            self.table[slot] = x

        elif self.collision_type == "Double":
            double_slot=self.double_hashing(x[0])
            probes = 0
            while self.table[slot] is not None:
                slot = (slot + double_slot) % self.table_size
                probes += 1
                if probes >= self.table_size:  # We've checked every slot
                    raise Exception("Table is full")
            self.table[slot] = x

        self.size+=1
    
    def find(self, key):
        slot=self.hash_function(key)
        #problem
        #Time complexity is O(|key| + table_size)
        #problem
        if self.collision_type == "Chain":
            for i in range(len(self.table[slot])):
                if key==self.table[slot][i][0]:
                    return self.table[slot][i][1]
            return None
        elif self.collision_type == "Linear":
            initial_slot = slot
            while self.table[slot] is not None:
                if self.table[slot][0] == key:
                    return self.table[slot][1]
                slot = (slot + 1) % self.table_size
                if slot == initial_slot:
                    return None
            return None

        elif self.collision_type == "Double":
            initial_slot = slot
            step_size = self.double_hashing(key)
            probes = 0
            while self.table[slot] is not None:
                if self.table[slot][0] == key:
                    return self.table[slot][1]
                slot = (slot + step_size) % self.table_size
                probes += 1
                if probes >= self.table_size:  # We've checked every slot
                    return None
            return None
    
    def get_slot(self, key):
        slot=self.hash_function(key)
        if self.collision_type == "Chain":
            if key in self.table[slot]:
                return slot
            else:
                return False
        elif self.collision_type == "Linear":
            initial_slot = slot
            while self.table[slot] is not None:
                if self.table[slot] == key:
                    return slot
                slot = (slot + 1) % self.table_size
                if slot == initial_slot:
                    return False
            return False

        elif self.collision_type == "Double":
            initial_slot = slot
            step_size = self.double_hashing(key)
            probes = 0
            while self.table[slot] is not None:
                if self.table[slot] == key:
                    return slot
                slot = (slot + step_size) % self.table_size
                probes += 1
                if probes >= self.table_size:  # We've checked every slot
                    return False
            return False
    
    def get_load(self):
        return self.size/self.table_size
    
    def __str__(self):
        if self.collision_type=="Chain":
            ans=""
            for i in range(self.table_size):
                if(self.table[i]!=None):
                    for j in self.table[i]:
                        ans=ans+'('+j[0]+','+j[1]+')'
                        ans=ans+';'
                    if(self.table[i] !=[]):
                        ans=ans[:-1]
                        ans=ans+'|'
                else:
                    ans=ans+"<EMPTY>|"
            return ans[:-1]
        
        else:  # For Linear and Double
            ans = ""
            for i in range(self.table_size):
                if self.table[i] is not None:
                    ans += '('+self.table[i][0]+','+ self.table[i][1]+')'+ '|'
                else:
                    ans += "<EMPTY>|"
            return ans[:-1]