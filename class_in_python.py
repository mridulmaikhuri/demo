class marks:
    def __init__(self,m1,m2,m3,m4,m5):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def  add(self):
        m=self.m1+self.m2+self.m3+self.m4+self.m5
        return "You have scored", m ,"marks out of 500"
    def __gt__(self,other):
        m=self.m1+self.m2+self.m3+self.m4+self.m5
        n=other.m1+other.m2+other.m3+other.m4+other.m5
        if m>n:
            return True
        else:
            return False
student1=marks(34,54,24,74,36)
student2=marks(23,98,45,34,99)
print(student1.add())
if student1>student2:
    print("student1 has scored more marks")
else:
    print("student 2 has scored more marks")
        
