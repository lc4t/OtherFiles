CC = g++
NAME = 4

CFLAGS = -g -lGLU -lGL -lglut -lm -L/usr/lib/X11 -lX11
targets = $(NAME)
obj = $(NAME).o

$(NAME): $(obj)
	$(CC) $(CFLAGS)  -o $(targets) $(obj)

$(NAME).o: $(NAME).cpp
	$(CC) $(CFLAGS) -c $(NAME).cpp


.PHONY : clean

clean:
	rm -f $(targets) $(obj)
