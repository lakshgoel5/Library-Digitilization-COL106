import hash_table as ht

# You can assume all added books will be different and have unique titles. 
# Furthermore, you can assume that the queried book in distinct_words or 
# count_distinct_words exists. We will not use testcases where these two conditions are not met.

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    

def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    # print(arr)
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k=l
    while(i< m-l+1 and j< r-m):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i < m-l+1:
        arr[k] = left[i]
        i+=1
        k+=1
    while j < r-m:
        arr[k] = right[j]
        j+=1
        k+=1
    return arr

def mergeSort_b(arr,text, l, r):
    # print(text)
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort_b(arr,text, l, m)
        mergeSort_b(arr,text, m+1, r)
        merge_b(arr,text, l, m, r)
    # print(text)

def merge_b(arr,text, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    left_text = text[l:m+1]
    right_text = text[m+1:r+1]
    i = j = 0
    k=l
    while(i< m-l+1 and j< r-m):
        if left[i] < right[j]:
            arr[k] = left[i]
            text[k] = left_text[i]
            i+=1
        else:
            arr[k] = right[j]
            text[k] = right_text[j]
            j+=1
        k+=1
    while i < m-l+1:
        arr[k] = left[i]
        text[k] = left_text[i]
        i+=1
        k+=1
    while j < r-m:
        arr[k] = right[j]
        text[k] = right_text[j]
        j+=1
        k+=1
    return arr

def search(array, word):
    l=0
    r=len(array)-1
    while l<=r:
        m = l+(r-l)//2
        if array[m]==word:
            return m
        elif array[m]<word:
            l=m+1
        else:
            r=m-1
    return None


class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.book_titles = [0 for i in range(len(book_titles))]
        for i in range(len(book_titles)):
            self.book_titles[i]=book_titles[i]
        self.texts = [0 for i in range(len(texts))]
        for i in range(len(texts)):
            self.texts[i]=[0 for j in range(len(texts[i]))]
        for i in range(len(texts)):
            for j in range(len(texts[i])):
                self.texts[i][j]=texts[i][j]

        mergeSort_b(self.book_titles, self.texts, 0, len(self.book_titles)-1)
        for i in range(len(self.book_titles)):
            mergeSort(self.texts[i], 0, len(self.texts[i])-1)
        self.distinct=[[] for i in range(len(self.book_titles))]
        for i in range(len(self.book_titles)):
            for j in range(len(self.texts[i])):
                if j==0:
                    self.distinct[i].append(self.texts[i][j])
                elif self.texts[i][j]!=self.texts[i][j-1]:
                    self.distinct[i].append(self.texts[i][j])
    
    

    def distinct_words(self, book_title):
        l=0
        r=len(self.book_titles)-1
        required_index=0
        while l<=r:
            m = l+(r-l)//2
            if self.book_titles[m]==book_title:
                required_index=m
                break
            elif self.book_titles[m]<book_title:
                l=m+1
            else:
                r=m-1
        return self.distinct[required_index]
    
    def count_distinct_words(self, book_title):
        l=0
        r=len(self.book_titles)-1
        required_index=0
        while l<=r:
            m = l+(r-l)//2
            if self.book_titles[m]==book_title:
                # print(m)
                required_index=m
                break
            elif self.book_titles[m]<book_title:
                l=m+1
            else:
                r=m-1
        # print(len(self.distinct[required_index]))
        return len(self.distinct[required_index])
    
    def search_keyword(self, keyword):
        ans=[]
        for i in range(len(self.book_titles)):
            check=search(self.texts[i], keyword)
            if(check!=None):
                ans.append(self.book_titles[i])
        return ans
    
    def print_books(self):
        for book in range(len(self.book_titles)):
            print(self.book_titles[book], end='')
            print(':', end=' ')
            for j in range(len(self.distinct[book])-1):
                print(self.distinct[book][j], end=' | ')
            print(self.distinct[book][-1])

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.name=name
        self.book_name=[]
        if name=="Jobs":#O(table_size)
            self.hash_map = ht.HashMap("Chain", params)
        elif name=="Gates":
            self.hash_map = ht.HashMap("Linear", params)
        else:
            self.hash_map = ht.HashMap("Double", params)
    
    def add_book(self, book_title, text):#O(w+table_size)
        if self.name == "Jobs":#O(table_size)
            new_hash_set = ht.HashSet("Chain", self.hash_map.params)
            distinct_hash_set=ht.HashSet("Chain", self.hash_map.params)
        elif self.name == "Gates":
            new_hash_set = ht.HashSet("Linear", self.hash_map.params)
            distinct_hash_set=ht.HashSet("Linear", self.hash_map.params)
        else:
            new_hash_set = ht.HashSet("Double", self.hash_map.params)
            distinct_hash_set=ht.HashSet("Double", self.hash_map.params)
        
        for word in text: #O(w)
            new_hash_set.insert(word)
            if(not distinct_hash_set.find(word)):#O(1)
                distinct_hash_set.insert(word)
        self.book_name.append(book_title) #O(1)
        self.hash_map.insert((book_title, (new_hash_set, distinct_hash_set))) #O(1)
        
    #is load_factor always less than 1?
    def distinct_words(self, book_title): #O(k + table_size)
        hash_set = self.hash_map.find(book_title) #O(1)
        if hash_set:
            if self.name == "Jobs":
                ans=[]
                for i in hash_set[1].table: #O(table_size)
                    if i:
                        for j in i: #O(|i|)
                            ans.append(j)
                return ans
            else:
                ans=[]
                for i in hash_set[1].table: #O(table_size)
                    if i:
                        ans.append(i)
                return ans
        return None
    
    def count_distinct_words(self, book_title): #O(1)
        hash_set = self.hash_map.find(book_title) #O(1)
        if hash_set:
            return hash_set[1].size
        return 0
    
    def search_keyword(self, keyword): #O(k)
        ans=[]
        for book in self.book_name: #O(k)
            i=self.hash_map.find(book) #O(1)
            if i[1].find(keyword): #O(1)
                ans.append(book)
        return ans
    
    def print_books(self): #O(k*table_size)
        ans=""
        for book in self.book_name: #O(k)
            i=self.hash_map.find(book) #O(1)
            print(book, end='')
            print(':', end=' ')
            print(i[1]) #O(table_size)
