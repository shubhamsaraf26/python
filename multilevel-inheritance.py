class a:
    def a1(self,str1):
        self.str1=str1


class b(a):
    def b1 (self,str2):
        self.str2=str2

class c(b):
    def c1(self,str3):
        self.str3=str3

    def show_c1(self):
        print("class a ",self.str1)
        print("class b",self.str2)
        print("class c", self.str3)

c1=c()

c1.a1("str1")
c1.b1("str2")
c1.c1("hellow str3")

c1.show_c1()
