def update_insanity():
    global breakdown
    global insanedeath
    global name
    global gender
    if breakdown==0:
        print(" _________\n|_________|")
        print("Insanty is at 0.")
    elif breakdown==1:
        print(" _________\n||________|")
        print("Insanty is at 1.")
    elif breakdown==2:
        print(" _________\n|>|_______|")
        print("Insanty is at 2.")
    elif breakdown==3:
        print(" _________\n|>>|______|")
        print("Insanty is at 3.")
    elif breakdown==4:
        print(" _________\n|>>>|_____|")
        print("Insanty is at 4.")
    elif breakdown==5:
        print(" _________\n|>>>>|____|")
        print("Insanty is at 5.")
    elif breakdown==6:
        print(" _________\n|>>>>>|___|")
        print("Insanty is at 6.")
    elif breakdown==7:
        print(" _________\n|>>>>>>|__|")
        print("Insanty is at 7.")
    elif breakdown==8:
        print(" _________\n|>>>>>>>|_|")
        print("Insanty is at 8.")
    elif breakdown==9:
        print(" _________\n|>>>>>>>>||")
        print("Insanty is at 9.")
    elif breakdown==10:
        print(" _________\n|>>>>>>>>>|")
        isnanedeath=random.randint(1,3)
        if isnanedeath==1:
            print("{0} couldn't take it any more, so {1} stabbed {2}self.".format(name,himher,heshe))
        elif isnanedeath==2:
            print("{0} just lost their mind, so {1} choked {2}self to death.".format(name,himher,heshe))
        elif isnanedeath==3:
            print("{0} couldn't see the light at the end of the tunnel, so {1} hung {2}self on a noose nearby.".format(name,himher,heshe))
