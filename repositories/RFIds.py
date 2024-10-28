class RFIdsRepository:
    
    def __init__(self):
        self.ids = []

    def add(self, id):
        if(id):
            self.ids.append(id)

    def remove(self, id):
        if(id):
            self.ids.remove(id)

    def IdExists(self, id):
        return self.ids.index(id)

    def count(self):
        return len(self.ids)

    def getAll(self):
        return self.ids
        