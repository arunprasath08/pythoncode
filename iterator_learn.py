class myiteration():
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        while self.a<=20:
            try:
                x=self.a
                self.a+=2
            except:
                raise StopIteration
            else:
                return x

myIterationClass=myiteration()
myIterationClass_Iter=iter(myIterationClass)

# for i in range(6):
#     print(f" {i+1} ODD number:{next(myIterationClass)}")

for i in myIterationClass_Iter:
    print(f" {i+1} ODD number:{i}")

# name=['arun','prasath','suresh']
# name_iter=iter(name)
# for _ in name:
#     name_print=next(name_iter)
#     print(name_print)
