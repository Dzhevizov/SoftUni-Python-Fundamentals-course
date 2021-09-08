company_users = {}

users_info = input()

while not users_info == "End":
    company_name, user_id = users_info.split(" -> ")
    if company_name not in company_users:
        company_users[company_name] = []
    if user_id not in company_users[company_name]:
        company_users[company_name].append(user_id)
    users_info = input()

for company_name, users_list in sorted(company_users.items(), key=lambda x: x[0]):
    print(f"{company_name}")
    for user in users_list:
        print(f"-- {user}")
