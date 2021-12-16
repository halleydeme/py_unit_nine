class dog:
    def __init__(self,dog):
        self.name = dog
        self.trick_list = []


    def get_name(self):
        return self.name
    def sit(self):
        print( self.name + " sits")
        self.trick_list.append("sitting down")
    def eat_apples(self):
        print (self.name + " eat an apple")
        self.trick_list.append("eating apples")
    def do_a_wheel(self):
        print (self.name + " do a cartwheel ")
        self.trick_list.append("doing a cartwheel")

