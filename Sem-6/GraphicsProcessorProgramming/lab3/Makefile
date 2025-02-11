CC = nvcc
CFLAGS = -lpthread --Werror all-warnings
SRC = thread.cu
OUT = thread.out

all: build

build: $(SRC)
	$(CC) $(SRC) $(CFLAGS) -o $(OUT)

build-cuda-debug: CFLAGS += -g
build-cuda-debug: build

build-debug: CFLAGS += -DDEBUG
build-debug: build

build-debug-plus: CFLAGS += -DDEBUG -DDEBUGPLUS
build-debug-plus: build

clean:
	rm -rf $(OUT)
