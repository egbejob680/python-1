class phoneBook:
    def __init__(self,phoneBook):
        self.name = phoneBook
        self.records ={}
    def add(self,name,contact,address):
        self.records[name] = [contact,address]
    def getRecords(self,name):
        if name in self.records:
            return self.records[name]
        else:
            return None
phone = phoneBook("phone")
phone.add("abel","346747","wyydhh")
print("abel",(phone.getRecords("abel")[1]))

