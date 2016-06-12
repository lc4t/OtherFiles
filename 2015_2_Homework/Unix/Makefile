CC = gcc
CFLAGS = -g
targets = mtest
obj = mtest.o add.o sine.o cosine.o


mtest: $(obj)
		$(CC) $(CFLAGS) -o $(targets) $(obj)

mtest.o: mlib.h
add.o: add.h
sine.o: sine.h
cosine.o: cosine.h

.PHONY : clean

clean:
		rm -f $(obj)
