subscribers = set()
unsubscribers = set()

def add_email(email, set_name):
    set_name.add(email)
    print(f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(f"Email '{email}' removed from {set_name}.")
    else: 
        print(f"Email '{email}' not found")

def display_emails(set_name):
    for email in set_name:
        print(email)

def find_active_subscribers(set_subs, set_unsubs): 
    return set_subs.difference(set_unsubs)

add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
print("All Subscribers:")
print(subscribers)

print("All Unsubscribers:")
print(f"{display_emails(unsubscribers)}")

# Finding active subscribers
print("Active Subscribers:")
print(f"{find_active_subscribers(subscribers, unsubscribers)}")