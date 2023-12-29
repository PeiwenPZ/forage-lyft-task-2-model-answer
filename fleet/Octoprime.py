from fleet import Fleet

class Octoprime(Fleet):
    def __init__(self, wearSensors):
        #wearSensors is a list integer_list = [1, 0, 0.5, 1]
        self.wears = wearSensors
        
    def needs_service(self):

        counter = 0
        for wear in self.wears :
            counter= counter + wear
                
        if counter>=3.0:
            return True
        else:
            return False