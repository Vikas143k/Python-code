# a Python program to add a prefix text to all of the lines in a string
str="Humans have historically tended to separate civilization from wildlife in a number of ways, including the legal, so" \
    "cial, and moral senses. Some animals, however, have adapted to suburban environments. This includes such animals as" \
    " domesticated cats, dogs, mice, and rats. Some religions declare certain animals to be sacred, and in modern times," \
    " concern for the natural environment. It has provoked activists to protest against the exploitation of wildlife for" \
    " human benefit or entertainment."
prefix=input("Enter the prefix you want to add")
split1=str.split(".")
for i in split1:
    print(">",i)