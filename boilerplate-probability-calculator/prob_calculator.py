import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for (name,number) in kwargs.items():
            self.contents+=[name]*number
    def draw(self,number):
        if(number>len(self.contents)):
            return self.contents
        res=[]
        for i in range(number):
            a = random.randint(0, len(self.contents)-1)
            res.append(self.contents.pop(a))
        return res
    def draw_balls(self,number):
        if(number>len(self.contents)):
            return self.contents
        copy_contents = copy.copy(self.contents)
        res=[]
        for i in range(number):
            a = random.randint(0, len(copy_contents)-1)
            res.append(copy_contents.pop(a))
        return res
    



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m=0
    for n in range(num_experiments):
        
        draw_balls = hat.draw_balls(num_balls_drawn)
        # print(draw_balls)
        check = True
        for (key,num) in expected_balls.items():
            if(key not in draw_balls) or draw_balls.count(key) < num:
                check=False
        if(check):
            m+=1
            
   
    return m/num_experiments
