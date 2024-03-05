class Node: 
    def __init__(self,item, next):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.start = None

    def insert_at_start(self,item):
      
        self.start = Node(item,next= self.start )

    def insert_at_end(self,item):
        if self.start is None:
            self.start  = Node(item, None)
            return 
        itr = self.start
        while itr.next:
            itr = itr.next
        
        itr.next= Node(item, None)
    
    def get_length(self):
       count = 0
       itr = self.start
       while itr:
           itr = itr.next
           count =count+1
       print(f"The length of linklist list is {count}")
       return 
    
    def insert_at(self, index, item):
        if index<0  or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
           self.insert_at_start(self,item)
           return 
        count=0
        itr = self.head
        while itr:
             if count ==index-1:     
                 itr.next = itr.next.next
                 break
             itr = itr.next
             count+=1
if __name__=="__main__":
   abhi = LinkedList()
   abhi.insert_at_start("hi")
   abhi.insert_at_end("hello")
   abhi.insert_at_start("bye")
   abhi.get_length()
