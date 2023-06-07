import os
from datetime import datetime
import readline
from unidecode import unidecode


orange = "\033[0;33m"
white = "\033[0;37m"
green = "\033[0;32m"


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

    return category_name, ctf_name, chall_cat_name, filename


def create_file(file_path, real_name):

    category_name, ctf_name, chall_cat_name, filename = get_paths(file_path)
    #print("category_name: {}, ctf_name: {}, category_name: {}, chall_name: {}".format(category_name, ctf_name, category_name, chall_name))

    # put the first letter of category_name, ctf_name, chall_cat_name and chall_name in uppercase
    upper_category_name = category_name[0].upper() + category_name[1:]
    upper_ctf_name = ctf_name[0].upper() + ctf_name[1:]
    upper_chall_cat_name = chall_cat_name[0].upper() + chall_cat_name[1:]
    upper_chall_name = filename[0].upper() + filename[1:] 


    title = f"{upper_category_name} | {upper_ctf_name} | {upper_chall_cat_name} | {real_name}"
    print("title: {}".format(title))

    author = input("Author: ")
    date = datetime.today().strftime('%Y-%m-%d')
    categories = [upper_category_name, upper_ctf_name, upper_chall_cat_name]
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
        
        # List of words for autocompletion
        categories = os.listdir(os.path.join(base_dir, current_dir))

        # Custom completer function
        def completer(text, state):
            options = [word for word in categories if word.startswith(text)]
            if state < len(options):
                return options[state]
            else:
                return None

        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")

        arrow = " -> "

        global orange, white, green
        cmd_color = orange
        arrow_color = white
        instruction_color = green

        prompt = cmd_color + "Create file here"
        prompt += arrow_color + arrow
        prompt += instruction_color + "'exit',\n"
        prompt += cmd_color + "Create a new folder"
        prompt += arrow_color + arrow
        prompt += instruction_color + "type its name,\n"
        prompt += cmd_color + "Navigate to a folder"
        prompt += arrow_color + arrow
        prompt += instruction_color + "type its name\n"
        prompt += white + "\n"
        prompt += "Available folders:\n"

        category = input("{}{}\n> ".format(prompt, "\n".join(categories)))
        print()

        if category == "exit":
            break
        if category in categories:
            current_dir = os.path.join(base_dir, current_dir, category)
        else:
            create_dir(base_dir, current_dir, category)
    return current_dir


def main():

    work_dir = os.getcwd()

    path = choose_or_create_category(work_dir)

    global orange, white, green
    print(green + "\nYour path is: " + white + path)
    real_name = input(green + "Choose a name for your article:\n" + white + "> ")

    filename = real_name.strip().lower().replace(" ", "_").replace("'", "_").replace(",", "")
    filename = unidecode(filename)

    date = datetime.today().strftime('%Y-%m-%d')
    

    filename = "{}-{}.md".format(date, filename)

    confirm = input(green + "Do you want to create a file named " + white + filename + green + "? Y/[N]:\n" + white)

    if confirm == "y" or confirm == "Y":
        file_path = os.path.join(path, filename)
        create_file(file_path, real_name)
        print("File created")



if __name__ == "__main__":
    main()

