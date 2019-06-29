class Node():

    def __init__(self,value,p=0):
        self.data = value
        self.next = p

class LinkList():

    def __init__(self):
        self.head = 0


    def initlist(self,a1):
        self.head = Node(a1[0])


        # if self.head == 0:


        #
        # else:
        p = self.head

        for i in a1[1:]:

            p.next = Node(i)
            p = p.next
    def append_list(self,values):


        # q = Node(values)
        # if l.get_leng() ==0:
        #     self.head = q
        # else:
        #     p = self.head
        #     while p.next!=0:
        #         p = p.next
        #     p.next = q
        q = Node(values)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                print(p.data)
                p = p.next
            p.next = q

    def get_leng(self):
        if self.head ==0:
            print("no")
        p = self.head
        print('*' * 100)
        print(p.data)
        a = 0
        while p:
            print(p.data)

            p = p.next

            a+=1
        print(self.head.data)
        return a
    def is_empty(self):
        if self.get_leng() == 0:
            return True
        else:

            return False

    def insert(self,index,values):
        if index == 0:
            q = self.head
            self.head = Node(values)
            self.head.next = q.next
        else:
            post = self.head
            p = self.head
            j = 0
            while p.next!=0 and j<index:
                post = p
                p = p.next
                j+=1
            if j ==index:
                x = Node(values)
                x.next = p
                post.next = x


    def delete(self,index):

        p = self.head
        if self.head == 0:
            print('列表为空')
        if index == 0:
            print('*'*100)
            print(p.next.data)
            self.head = p.next
            print('*'*100)
            print(self.head.data)

        else:
            post = self.head
            j = 0
            while p.next!=0 and j<index:
                post = p
                p = p.next
                j +=1
            if j == index:
                post.next = p.next







    # def is_empty(self):
    #     self.
    # def appendlist(self,value):





l = LinkList()
l.initlist([6,3,2,1,0])
# print(l.get_leng())
# l.is_empty()
# l.append_list(8)
# l.append_list(8)
l.insert(1,10)
print(l.get_leng())




