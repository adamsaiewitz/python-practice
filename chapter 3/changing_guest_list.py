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
