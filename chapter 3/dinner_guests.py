guests = ['steve jobs', 'bob hope', 'johnny cash']

jobs_message = "Hey " + guests[0].title() + "! Come eat my food!"
hope_message = "Hey " + guests[1].title() + "! Come eat my food!"
cash_message = "Hey " + guests[2].title() + "! Come eat my food!"

print(jobs_message)
print(hope_message)
print(cash_message)

print("\n\nUnfortunately, " + guests[0].title() + " can't attend. Because he's dead.")

del guests[0]
guests.insert(0, 'bob dole')

jobs_message = "Hey " + guests[0].title() + "! Come eat my food!"

print(jobs_message)
print(hope_message)
print(cash_message)

print("Hey, we found a bigger dinner table!!")

guests.insert(0, 'tim cook')
guests.insert(2, 'jony ive')
guests.append('ezra koenig')

print("Come eat with me, " + guests[0].title())
print("Come eat with me, " + guests[1].title())
print("Come eat with me, " + guests[2].title())
print("Come eat with me, " + guests[3].title())
print("Come eat with me, " + guests[4].title())
print("Come eat with me, " + guests[5].title())

print("I have " + str(len(guests)) + " guests coming to dinner tonight.")
