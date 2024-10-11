print("This program will tell you the meanings of different crochet stitch abbreviations. It can also output a random type of stitch to learn!")
print("Note: This program uses American abbreviations.")
stitch = input('Please enter the stitch abbreviation, or enter "random" for a random type of stitch to learn. Enter "end" to exit.').lower()


while stitch != "end":
    if stitch == "sc":
        print("sc stands for single crochet!")
        print("This is the most basic stitch. Inside the chain, yarn over, then yarn over again.")
    elif stitch == "sl st" or stitch == "slst":
        print("sl st stands for slip stitch!")
        print("Inside the chain, yarn over through both loops on hook.")
    elif stitch == "hdc":
        print("hdc stands for half double crochet!")
        print("This is just like a single crochet but with an additional yarn over in the beginning.")
    elif stitch == "dc":
        print("dc stands for double crochet!")
        print("Careful not to confuse this with dec. This is similar to an hdc, but includes two yarn overs at the end. It's also a good idea to start with a few chains first.")
    elif stitch == "dec" or stitch == "sc2tog":
        print("dec stands for decrease!")
        print("This stitch is used to decrease the number of chains in a row. Instead of yarning through just one chain, yarn through the next one too.")
    elif stitch == "inc":
        print("inc stands for increase!")
        print("Simply do two of the desired stitch. Default is single crochet.")
    elif stitch == "tc":
        print("tc stands for triple crochet or treble crochet! Both are the same thing.")
        print("For this stitch, yarn over twice, then inside the chain, yarn over. Yarn over through two chains on hook, then yarn over through final three chains on hook.")
    elif stitch == "ch":
        print("ch stands for chain!")
        print("Yarn over once. That's it!")
    elif stitch == "dc2tog":
        print("dc2tog stands for a double crochet of two chains, aka a decrease with a double crochet!")
        print("Use the same steps you would for yarning over a dec/sc2tog, but do it in a double crochet stitch.")
    elif stitch == "dtr":
        print("dtr stands for double treble crochet!")
        print("Yarn over three times instead of twice at the beginning.")
    elif stitch == "tch":
        print("tch stands for turning chain. ")
        print("This is used at the end of a row when it is time to chain one and turn your work.")
    elif stitch == "bp":
        print("bp stands for back post!")
        print("Crochet into the back post, which sits behind the current chains in the work.")
    elif stitch == "blo":
        print("blo stands for back loop only!")
        print("This stitch can create a wobbly effect. instead of crocheting across the whole chain, crochet only into the one further back.")
    elif stitch == "fp":
        print("fp stands for front post!")
        print("Crochet into the front post, which sits in front of the current chains int he work")
    elif stitch == "yo":
        print("yo stands for yarn over. Pull the yarn through the work!")
    elif stitch == "yoh":
        print("yoh stands for yarn over hook!")
        print("This is a specific type of yarn over where you go over the hook.")
    elif stitch == "yu":
        print("yu stands for yarn under!")
        print("pull the yarn while it is under your hook.")
    elif stitch == "ws":
        print ("ws stands for wrong side. It is often used in patterns in order to get a specific shape or style.")
    elif stitch == "rs":
        print("rs stands for right side. It is often used in patterns in order to get a specific shape or style. ")
    elif stitch == "sk":
        print("sk stands for skip! When you see this, all you need to do is skip that next chain. ")
    elif stitch == "end":
        print("")
    else:
        print("Sorry! Either I don't know that stitch, or something was written incorrectly.")

    stitch = input('Please enter the stitch abbreviation, or enter "random" for a random type of stitch to learn. Enter "end" to exit.').lower()

