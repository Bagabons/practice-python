
class Cat:
    

    def __init__(self, name: str) -> None:
        self.name = name
        pass

    def meow(self):
        print(self.name)

    def do_loop(self):
        
        
        user_input = input("what is the password?")
        while (user_input != "missionisthebest"):
            if (user_input == "suckmyballs"):

                print ("suckthemthen")
                return    
        
            user_input = input("wrong! WHAT IS THE ANSWER!?")



        print("you are allowed in.")



    def do_math(self,a: int, b:int) -> int:
        c = (a + b) * a
        return c


    def do_logic(self):
        name = input("what is your name?")
        size_of_name = len(name)
        if (size_of_name % 2 == 0):
            print("you're a genius!")

        else:
            print("you're a loser!")





cat = Cat("mission")


cat.meow()
result = cat.do_math(5,2)
print(result)
cat.do_loop()