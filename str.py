class Node:
    def __init__(self, value = None):
       self.value = value
       self.next = None

class LinkedString():
    def __init__(self, s = None):
        self.root = self.__get_list(s)
       
    def __get_list(self, s):
        if len(s) == 0:
            return None
        else:
            n = Node(s[0])
            n.next = self.__get_list(s[1:])
            return n
         
    def print(self):
        self.__print_list(self.root)

    def __print_list(self, p):
        if p != None:
            print(p.value, end='')
            self.__print_list(p.next)


if __name__ == '__main__':
    mystr = 'Hello'
    ll = LinkedString(mystr)
    ll.print()
            
