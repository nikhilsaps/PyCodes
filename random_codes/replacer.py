# this code will  run to check the  nihil text  file then  replace  the given word with given word

def file_to_string():
    f= open("nikhil.txt","r+")
    txt= f.read().lower()
    f.close()
    return txt
def replace(find,repl):
    new_txt=file_to_string().replace(find,repl)
    f =open("nikhil.txt","w")
    f.truncate()
    f.write(new_txt)
    f.close()

def main():
    find= input("what you want to replace ")
    repl= input("what you want new word ")
    replace(find,repl)

if __name__ == "__main__":
    main()