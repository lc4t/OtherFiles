CC = gcc
CFLAGS = -g
target = main
obj = main.o Stack.o

main: $(obj)
	$(CC) $(CFLAGS) -o $(target) $(obj)

main.o: Stack.h
	$(CC) $(CFLAGS) -c main.c

Stack.o: Stack.h
	$(CC) $(CFLAGS) -c Stack.c

.PHONY : clean r

clean:
	rm -f $(obj) $(target)
