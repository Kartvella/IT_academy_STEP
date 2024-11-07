#LinkedList

class Node:
    def __init__(self, data=None):
        #კვანძში მოთავსებული მონაცემი
        self.data = data
        #შემდეგი კვანძი, რომელიც საწყისისთვის იქნება None
        self.next = None


class LinkedList:
    def __init__(self):
        #პირველი კვანძი(ჩავთვლით, რომ თავიდან არ ცარიელია)
        self.head = None

    def append(self, data):
        # ვქმნით ახალ კვანძს 
        new_node = Node(data)
        #თუ პირველი კვანძი ცარიელია
        if self.head is None:
            #პირველი კვანძის მნიშვნელობა გახდება ახალი კვანძი
            self.head = new_node
            #გამოვალთ ფუნქციიდან, რადგან ლოგიკა დავასრულეთ
            return
        #თუ head ცარიელი არაა, ჩავთვლით, რომ ბოლო კვანძი არის ლისტის head
        last_node = self.head
        #while ბოლო კვანძის შემდეგი კვანძი ცარიელი არაა
        while last_node.next:
            #ბოლო კვანძი გახდება შემდეგი კვანძი
            last_node = last_node.next
        #როცა ლუპიდან გამოვალთ, ბოლო კვანძის შემდეგი კვანძი None იქნება
        #და მაგის ადგილზე ჩავსვამთ ახალ კვანძს
        last_node.next = new_node
        #მეთოდი მოქმედებს .append()-ის იდენტურად, თუმცა დაკავშირებულ ლისტებზე

    def remove_at(self, index):
        #თუ ინდექსი ნაკლებია 0-ზე და head ცარიელია
        if index < 0 and self.head is None:
            #მაშინ ფუნქციას დავასრულებთ, რადგან არასწორი ინდექსი გვაქვს, ან წასაშლელი ცარიელია
            return
        #თუ ინდექსი == 0
        if index == 0:
            #მაშინ head გახდება მისი შემდეგი კვანძი და ის ავტომატურად წაიშლება
            self.head = self.head.next
            return
        #თუ ინდექსი != 0, ჩავთვალოთ, რომ მიმდინარე კვანძი head-ია 
        current_node = self.head
        #და მიმდინარე პოზიცია = 0
        current_position = 0
        #while მიმდინარე კვანძს გააჩნია მომდევნო კვანძი და მიმდინარე პოზიცია ნაკლებია ინდექსით მინუს ერთზე
        while current_node.next and current_position < index - 1:
            #მიმდინარე კვანძი გახდება მომდევნო
            current_node = current_node.next
            #და პოზიცია მოიმატებს ერთით
            current_position += 1
        if current_node.next:
            current_node.next = current_node.next.next
        '''48-57 ხაზებმა იმოქმედეს შემდეგნაირად:
        დავუშვათ წასაშლელი გვაქვს კვანძი, რომლის ინდექსია 5. 
        როდესაც ლუპიდან გამოვალთ, ჩვენი current node იქნება კვანძი (ინდექსით 4).
        56-57 ხაზები კი იმას უზრუნველყოფენ, რომ მეოთხე ინდექსის მქონე კვანძის 
        შემდეგი კვანძი გახდეს შემდეგის შემდეგი, ამ შემთხვევაში, 4-ის შემდეგის შემდეგი
        ანუ 6. ინდექსით მეხუთე კვანძი კი ავტომატურად წაიშლება.    
        '''

    def display(self):
        #მიმდინარე კვანძი არის head(საწყისი)
        current_node = self.head
        #while მიმდინარე კვანძი ცარიელი არაა
        while current_node is not None:
            #დავპრინტავთ მიმდინარე კვანძის მონაცემს
            print(current_node.data, end=' -> ')
            #მიმდინარე კვანძი გახდება შემდეგი კვანძი
            current_node = current_node.next

    def add_by_index(self, data, index):
        if index < 0:
            return
        new_node = Node(data)
        #თუ ინდექსი == 0-ს
        if index == 0:
            #ახალი კვანძის შემდეგი იქნება head
            new_node.next = self.head
            #და head იქნება ახალი კვანძი
            self.head = new_node
            return

        curr_node = self.head
        curr_position = 0
        #while მიმდინარე კვანძს გააჩნია მომდევნო კვანძი და მიმდინარე პოზიცია ნაკლებია ინდექსით მინუს ერთზე
        while curr_node.next and curr_position < index - 1:
            #მიმდინარე კვანძი გახდება მომდევნო
            curr_node = curr_node.next
            #და პოზიციაც მოიმატებს ერთით
            curr_position += 1
        #თუ კვანძი ცარიელია
        if curr_node is None:
            print("index out of bounds")
            return
        #ახალი კვანძის მომდევნო იქნება მიმდინარე კვანძის მომდევნო
        new_node.next = curr_node.next
        #და მიმდინარე კვანძის მომდევნო იქნება ახალი კვანძი
        curr_node.next = new_node
    
    def remove_by_val(self, val):

        if self.head is None:
            print("list is empty")
            return
        #თუ head-ის მონაცემი == val-ს
        if self.head.data == val:
            #head გახდება მისი მომდევნო
            self.head = self.head.next
            return

        curr_node = self.head
        #while მიმდინარე კვანძს მომდევნო გააჩნია
        while curr_node.next:
            #თუ მიმდინარე კვანძის მომდევნო == val-ს
            if curr_node.data == val:
                #მიმდინარე კვანძის მომდევნო გახდება მისი მომდევნოს მომდევნო
                curr_node.next = curr_node.next.next
                return
            #მიმდინარე კვანძი გახდება მისი მომდევნო, რათა ლისტის ყველა კვანძი შემოწმდეს
            curr_node = curr_node.next
        #თუ value ლუპით ვერ მოიძებნა, მაშინ არ ლისტში არ არის
        print("value not found in the list")



linked_list = LinkedList()

linked_list.append(10)
linked_list.append(5)
linked_list.append(25)
linked_list.append(12)
linked_list.append(11)

linked_list.add_by_index(100, 2)
linked_list.display()
print()
linked_list.remove_by_val(100)
linked_list.display()

print()
linked_list.remove_at(2)
linked_list.display()
print()
linked_list.remove_at(2)
linked_list.display()


#Stack

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None
        self.length = 0

    def empty(self):
        #თუ სტეკის ობიექტის სიგრძე == 0-ს, მაშინ სტეკი ცარიელია და დააბრუნებს True-ს
        return self.length == 0

    def size(self):
        #მეთოდი აბრუნებს სტეკის სიგრძეს
        return self.length

    def push(self, data):
        #შეიქმნება ახალი კვანძი
        new_node = Node(data)
        #ახალი კვანძის შემდეგი კვანძი იქნება top node
        new_node.next = self.top_node
        #top node იქნება ახალი კვანძი
        self.top_node = new_node
        #სტეკის სიგრძე მოიმატებს ერთით
        self.length += 1

    def pop(self):
        #თუ სტეკი ცარიელი არაა
        if not self.empty():
            #ამოვარდნილი ელემენტი იქნება top node-ის მონაცემი
            popped_item = self.top_node.data
            #top node გახდება მაგის შემდეგი კვანძი
            self.top_node = self.top_node.next
            #სტეკის სიგრძე შემცირდება ერთით
            self.length -= 1
            #დაბრუნდება ამოვარდნილი ელემენტი
            return popped_item
        #თუ არა
        else:
            #დაიპრინტება ინდექსის ერორი
            raise IndexError('Stack is empty')


stack = Stack()
# print(stack.empty())
# print(stack.size())

stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
# print(stack.empty())
# print(stack.size())


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.empty())
# print(stack.size())