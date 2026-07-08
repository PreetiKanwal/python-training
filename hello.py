name = input("What's your name? ")

#remove whitespace from str 
name = name.strip()
# we are passing two argument in this" hello" , name 
print("hello,", name)

#we are passing single argument here 
print("hello, "+name )
#this will show name in next line , because official documentation of print had end="\n" to move to the next line.
print("hello,")
print(name)
#by passing no value in end we made it not to end the line there are name can be written alongside hello.
print("hello, ", end="")
print(name)
# f in the begining of " tells python this is a special  string . you need to format this in special way.
print(f"hello, {name}")

#if you want "" with text you can either change outter qoutation to '' . or 
print('hello,"friend"')
# you can use '\' escape character , \followed by the character you want to insert into a string literal.
print("hello, \"friend\"")