#Parent Class PetID
class Owner:
    name = "Kelsey"
    email = "KelseyL@gmail.com"
    phone_number = "666-666-6666"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email:")
        entry_phone = input("Enter your phone number:")
        if (entry_email == self.email and entry_phone == self.phone_number):
            print("Welcome {}".format(entry_name))
        else:
            print("We don't have you in our database")
#Child class pet info
class pet(Owner):
    pet = "Spot"
    Pettype = "dog"
    pin = "1234"
#adding second login
    def getLoginInfo(self):
        entry_pet = input("Enter your pets name: ")
        entry_pettype = input("Enter your pet type:")
        entry_pin = input("Enter pin:")
        if (entry_pet == self.pet and entry_pin == self.pin):
            print("Awesome Kelsey! Looks like we have {} on file!".format(entry_pet))
        else:
            print("We don't have your pet in our database")
#adding pet instructions

class instructions(Owner):
     def food(Owner):
         print("spot eats dry kibble")
     def grooming(Owner):
         print("spot gets brushed once a day")
     def medications(Owner):
         print("Spot doesn't have any medications")
         

customer = Owner()
customer.getLoginInfo()

alternative = pet()
alternative.getLoginInfo()

alternative1 = instructions()
alternative1.food()
alternative1.grooming()
alternative1.medications()


    
                          
