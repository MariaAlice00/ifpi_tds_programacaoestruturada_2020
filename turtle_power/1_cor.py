from turtle import * 

def main():
    shape('turtle') 
    speed(8)

    purple()
    orange()

    done() 


def purple():
    color('Purple')
    pensize(7) 
    
    right(90) 
    forward(100) 
    left(90)
    forward(50)


def orange():
    color('Orange')
    pensize(3)
    
    penup() 
    forward(50)
    pendown() 
    forward(50)


if __name__ == "__main__":
    main()
