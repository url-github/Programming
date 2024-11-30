def save_user_data(**kwargs):
    data = kwargs
    print("User data:", data)

    user_data = r"/Users/p/Documents/Scripts/Programming/068-args-kwargs/user_data.txt"

    with open(user_data, mode="a", encoding="utf-8") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

save_user_data(name="John Doe", age=30, occupation="Engineer", city="New York")
save_user_data(name="Jane Smith", age=25, occupation="Designer", city="Los Angeles")