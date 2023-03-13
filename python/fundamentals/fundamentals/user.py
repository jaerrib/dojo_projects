class User():

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        # Prints all of the users' details on separate lines
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Is reward member:", self.is_reward_member)
        print("Gold card points:", self.gold_card_points)

    def enroll(self):
        """
        Changes the user's member status to True and set their gold card points to 200
        Check if they are a member already, and if they are, print "User already a
        member." and return False, otherwise return True.
        """
        if self.is_reward_member == True:
            print("User already a member")
            return False
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            return True

    def spend_gold_points(self, amount):
        """
        Decreases the user's points by the amount specified
        Checks to be sure they have enough points to spend that amount
        and handle appropriately.
        """
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            # print(self.gold_card_points,"gold card points left")
        else:
            print("Not enough gold points")

user1 = User("John", "Doe", "jdoe@domain.com", 18)
user1.enroll()
user2 = User("Jane", "Doe", "jane_doe@domain.com", 21)
user3 = User("Linus", "Torvalds", "linuxguru@domain.com", 53)
user1.spend_gold_points(50)
user2.enroll()
user2.spend_gold_points(80)
user1.display_info()
user2.display_info()
user3.display_info()
user1.enroll()
user3.spend_gold_points(40)