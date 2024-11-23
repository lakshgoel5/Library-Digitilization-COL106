from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        new_size = get_next_size()
        # Update table size and params
        self.table_size = new_size
        if self.collision_type == "Chain" or self.collision_type == "Linear":
            self.params = (self.z, self.table_size)
        else:  # Double hashing
            self.params = (self.z1, self.z2, self.c2, self.table_size)
        
        # Initialize new table based on collision type
        if self.collision_type == "Chain":
            self.table = [[] for _ in range(new_size)]
        else:
            self.table = [None for _ in range(new_size)]
        
        # Reset size counter
        self.size = 0
        
        # Reinsert all elements using super().insert()
        if self.collision_type == "Chain":
            for chain in old_table:
                for key in chain:
                    super().insert(key)
        else:
            for key in old_table:
                if key is not None:
                    super().insert(key)
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        new_size = get_next_size()
        
        # Update table size and params
        self.table_size = new_size
        if self.collision_type == "Chain" or self.collision_type == "Linear":
            self.params = (self.z, self.table_size)
        else:  # Double hashing
            self.params = (self.z1, self.z2, self.c2, self.table_size)
        
        # Initialize new table based on collision type
        if self.collision_type == "Chain":
            self.table = [[] for _ in range(new_size)]
        else:
            self.table = [None for _ in range(new_size)]
        
        # Reset size counter
        self.size = 0
        
        # Reinsert all elements
        if self.collision_type == "Chain":
            for chain in old_table:
                for pair in chain:  # pair is (key, value)
                    super().insert(pair)  # HashMap's insert expects a (key, value) tuple
        else:
            for pair in old_table:
                if pair is not None:
                    super().insert(pair)  # pair is already (key, value)
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()