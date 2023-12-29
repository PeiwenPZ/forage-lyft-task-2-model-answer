from fleet import Fleet

class Carrigan(Fleet):
    def __init__(self, wearSensors):
        #wearSensors is a list integer_list = [1, 0, 0.5, 1]
        self.wears = wearSensors
        
    def needs_service(self):

        counter = 0
        for wear in self.wears :
            if wear >= 0.9:
                counter+=1
                
        if counter>1:
            return True
        else:
            return False
        
