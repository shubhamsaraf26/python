class parent1:
    def assign1(self,str1):
        self.str1=str1

class parent2:
    def assign2(self,st2):
        self.str2=st2


class parent(parent1,parent2):
    def assign3(self,str3):
        self.str3=str3

    def show3(self):
        print("str1",self.str1)
        print("str2",self.str2)
        print("str3",self.str3)


s1=parent()

s1.assign1("str1")
s1.assign2("str2")
s1.assign3("str3")

s1.show3()