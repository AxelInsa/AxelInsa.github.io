import os
from datetime import datetime


def get_paths(file_path):
    filename_path = os.path.dirname(file_path)
    chall_cat_path = os.path.dirname(filename_path)
    ctf_path = os.path.dirname(chall_cat_path)
    category_path = os.path.dirname(ctf_path)

    filename = os.path.basename(filename_path)
    chall_name = os.path.basename(filename_path)
    chall_cat_name = os.path.basename(chall_cat_path)
    ctf_name = os.path.basename(ctf_path)
    category_name = os.path.basename(category_path)

    # put the first letter of category_name, ctf_name, chall_cat_name and chall_name in uppercase
    category_name = category_name[0].upper() + category_name[1:]
    ctf_name = ctf_name[0].upper() + ctf_name[1:]
    chall_cat_name = chall_cat_name[0].upper() + chall_cat_name[1:]
    chall_name = chall_name[0].upper() + chall_name[1:] 

    return category_name, ctf_name, chall_cat_name, filename


def create_file(file_path, real_name):

    category_name, ctf_name, chall_cat_name, filename = get_paths(file_path)
    #print("category_name: {}, ctf_name: {}, category_name: {}, chall_name: {}".format(category_name, ctf_name, category_name, chall_name))

    title = f"{category_name} | {ctf_name} | {chall_cat_name} | {real_name}"
    print("title: {}".format(title))

    author = input("Author: ")
    date = datetime.today().strftime('%Y-%m-%d')
    categories = [category_name, ctf_name, chall_cat_name]
    tags = categories
    permalink = f"/{category_name}/{ctf_name}/{chall_cat_name}/{filename}"

    with open(file_path, "w") as f:
        f.write("---\n")
        f.write("title: {}\n".format(title))
        f.write("author: {}\n".format(author))
        f.write("date: {}\n".format(date))
        f.write("categories: {}\n".format(categories))
        f.write("tags: {}\n".format(tags))
        f.write("permalink: {}\n".format(permalink))
        f.write("---\n")
    

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
    real_name = input("Choose a name for your article\n> ")

    filename = real_name.strip().lower().replace(" ", "_").replace("'", "_")

    date = datetime.today().strftime('%Y-%m-%d')
    

    filename = "{}-{}.md".format(date, filename)

    confirm = input("Do you want to create a file named {}? y / n\n".format(filename))

    if confirm == "y" or confirm == "Y":
        file_path = os.path.join(path, filename)
        create_file(file_path, real_name)
        print("File created")



if __name__ == "__main__":
    main()

