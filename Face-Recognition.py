for i in range(50):
    print("##########Welcome to face recognition system############")
    print("press 1 to check age")
    print("press 2 to check gender")
    print("press 3 to check race")
    print("press 4 to check emotion")
    print("press 5 to check AGE,GENDER,RACE,EMOTION")
    print("press 6 to check to verifiy face")
    a=int(input("please enter your choice\t="))
    b=str(input("write location of image\t="))
    from deepface import DeepFace
    from PIL import Image
    print("")
    print("")
    print("")
    print("")
    print("")
    if a==1:
        im = Image.open(b)
        im.show() 
        obj = DeepFace.analyze(img_path = b, actions = ['age'])
        print("Age of the person=\t",obj)
    elif a==2:
        im = Image.open(b)
        im.show() 
        obj = DeepFace.analyze(img_path = b, actions = ['gender'])
        print("Gender of the person=\t",obj)
    elif a==3:
        im = Image.open(b)
        im.show() 
        obj = DeepFace.analyze(img_path = b, actions = ['race'])
        print("Race of the person=\t",obj)
    elif a==4:
        im = Image.open(b)
        im.show() 
        obj = DeepFace.analyze(img_path = b, actions = ['emotion'])
        print("Emotion of the person=\t",obj)
    elif a==5:
        im = Image.open(b)
        im.show() 
        obj = DeepFace.analyze(img_path = b, actions = ['age'])
        print("Age of the person=\t",obj)
        print("")
        obj = DeepFace.analyze(img_path = b, actions = ['gender'])
        print("Gender of the person=\t",obj)
        print("")
        obj = DeepFace.analyze(img_path = b, actions = ['race'])
        print("Race of the person=\t",obj)
        print("")
        obj = DeepFace.analyze(img_path = b, actions = ['emotion'])
        print("Emotion of the person=\t",obj)
        print("")
    elif a==6:
        im = Image.open(b)
        im.show() 
        c=str(input("write location of Second Image\t="))
        im = Image.open(c)
        im.show() 
        result = DeepFace.verify(img1_path = b, img2_path = c)
        print(result)

