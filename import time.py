import time
import tracemalloc
class node:
    def _init_ (self,data):
       print("node created",data)
       self.data=data
       self.next=None
class S_L_List:
    def _init_ (self):
        self.head=None
        self.ctr=0
    def insert_beginning(self,data):
        node=node(data)
        if self.head==None:
            self.head=node
            self.ctr+=1
        else:
            node.next=self.head
            self.head=node
            self.ctr+=1
            print("Node inserted",data)
        return
    def insert_middle(self,pos,data):
        if pos==0:
            self.insert_beginning(data)
        elif pos==self.ctr+1:
            self.insert_end(data)
        else:
            node=node(data)
            temp=self.head
            i=0
            while (i<pos-1):
                temp=temp.next
                i+=1
            node.next=temp.next
            temp.next=node
            self.ctr+=1
            print("node inserted",data)
        return
    def inserted_end(self,data):
        node=node(data)
        node.next=None
        if self.head==None:
            self.head=node
            return
        temp=self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=node
        self.ctr+=1
        print("node inserted",data)
        return
    def delete_middle(self,pos):
        if self.head==None:
            print("no nodes exist")
        elif pos==0:
            self.delete_beginning()
        elif pos==self.ctr:
            self.delete_end()
        else:
            temp=self.head
            prev=temp
            i=0
            while (i<pos):
                prev=temp
                temp=temp.next
                i+=1
                prev.next=temp.next
                print("node deleted",temp.data)
                temp.next=None
                self.ctr-=1
            return
    def delete_end(self):
            if self.ctr==0:
                print("no nodes present")
            elif self.ctr==1:
                self.ctr=0
                print("node deleted",self.head.data)
                self.head=None
            else:
                temp=self.head
                prev=self.head
                while(temp.next is not None):
                    prev=temp
                    temp=temp.next
                print("node deleted",temp.data)
                temp.data=None
                temp.next=None
                self.ctr-=1
                return
    def traversal_forward(self):
                if self.head==None:
                    print("no nodes exist")
                print("traversal forward")
                temp=self.head
                while(temp is not None):
                    print(temp.data)
                    temp=temp.next
    def display(self):
                if self.head==None:
                    print("empty")
                else:
                    temp=self.head
                    while temp:
                        print(temp.data,end='-->')
                        temp=temp.next
                    print("NULL")
    def search(self,key):
                temp=self.head
                index=0
                while temp:
                    if temp.data==key:
                        return index
                    temp=temp.next
                    index+=1
                return-1
def menu():
                print("1.Insert at beginning")
                print("2.Insert at end")
                print("3.Delete at beginning")
                print("4.Delete at end")
                print("5.Delete at middle")
                print("6.Delete at end")
                print("7.Traversal forward")
                print("8.Count number of nodes")
                print("9.Display")
                print("10.Search")
                print("11.Exit")
                ch=eval(input("Enter choice:"))
                return ch
print("************SINGLE LINKED LIST************")
I=S_L_List()
start=time.process_time()
tracemalloc.start()
while True:
    ch=menu()
    if ch==1:
      data=eval(input("enter data:"))
      I.insert_beginning(data)
    elif ch==2:
      data=eval(input("enter data:"))
      pos=eval(input("enter the position:"))
      I.insert_middle(pos,data)
    elif ch==3:
      data=eval(input("enter data:"))
      I.insert_end(data)
    elif ch==4:
      I.delete_be1ginning()
    elif ch==5:
      pos=eval(input("enter position:"))
      I.delete_middle(pos)
    elif ch==6:
      I.delete_end()
    elif ch==7:
      I.traverse_forward()
    elif ch==8:
        print("number of nodes",I.ctr)
    elif ch==9:
        print("List:",end="")
        I.display()
        print("\n")
    elif ch==10:
        key=int(input("enter item to search:"))
        i=I.search(key)
        if i>=0:
            print("item found at index position",i)
        else:
            print("item not in the list\n\n")
    else:
      print("exit")
      break
print("Space required=",tracemalloc.get_traced_memory())
end=time.process_time()
print("Time required=",(end-start))
tracemalloc.stop()
print("testing:")
                        



                    








        


            



