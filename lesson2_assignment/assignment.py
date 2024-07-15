from PIL import Image

def check_devision():
    try:
        a = 1/0
    except ZeroDivisionError as e:
        print("devision by zero")

def check_code_legal():
    try:
        x = 1
    finally:
        print("finally")

def working_with_file():

    with open("myfile.txt","a") as f:
        f.write("Evgeny is my name")

    with open("myfile.txt","r") as f:
        line = f.readlines()
        print(line)

def working_with_picture():

    im = Image.open('2.png')
    out = im.point(lambda i: i * 5)
    out.show()

working_with_picture()