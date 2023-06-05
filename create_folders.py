import os
from datetime import datetime

def create_dir(base_dir, current_dir, category):
    new_dir = os.path.join(current_dir, category)
    confirm = input("Do you want to create a folder named {}? y / n\n".format(category))
    
    if (confirm == "y" or confirm == "Y") and not os.path.exists(new_dir):
        os.mkdir(new_dir)
        os.mkdir(os.path.join(base_dir, "assets", "img", os.path.relpath(current_dir, "_posts"), category))


def choose_or_create_category(base_dir):

    current_dir = "_posts"

    while True:
        categories = os.listdir(os.path.join(base_dir, current_dir))
        category = input("If you want to keep a path, type 'exit'\nIf you want to create a folder, type its name,\nElse choose a folder:\n{}\n> ".format("\n".join(categories)))

        if category == "exit":
            break
        if category in categories:
            current_dir = os.path.join(base_dir, current_dir, category)
        else:
            create_dir(base_dir, current_dir, category)
    return current_dir


def truncate_path(path):
    path_split = path.split("/")
    for i, value in enumerate(path_split):
        if value == "_posts":
            return path_split[i+1:]



def main():

    work_dir = os.getcwd()

    path = choose_or_create_category(work_dir)

    print("Your path is: {}".format(path))
    filename = input("Choose a name for your article\n> ")
    print("Your file will be named: {}".format(filename))

    date = datetime.today().strftime('%Y-%m-%d')
    

    filename = "{}-{}.md".format(date, filename)

    confirm = input("Do you want to create a file named {}? y / n\n".format(filename))

    if confirm == "y" or confirm == "Y":
        with open(os.path.join(path, filename), "w") as f:
            pass
        print("File created")



if __name__ == "__main__":
    main()

