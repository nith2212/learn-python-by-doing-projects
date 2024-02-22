name=input("Enter your name: ")
print(f"Hello, {name}! You want to know what taylor swift song are you based on your choice of adjectives? Let's find out!")

adj1=str(input("Choose any one adjective, type it out exactly as displayed:Cheerful or Loyal or Bold "))
adj2=str(input("Choose any one adjective, type it out: Sad or Wise or Angry "))
verb=str(input("Enter a verb of your choice: "))



if adj1=="Cheerful":
    trait1="Shake it off"

elif adj1=="Loyal":
    trait1="Love Story"

else:
    trait1="Sparks Fly"


if adj2=="Sad":
    trait2="You're Losing Me"

elif adj2=="Wise":
    trait2="You're On Your Own Kid"

else:
    trait2="Better Than Revenge"


print(f" Okay! Now let us see what songs are you! You are....... drumroll..... {trait1} and {trait2}!!! Wowwww, I bet you feel like you want to {verb}! Haha I feel you!")

