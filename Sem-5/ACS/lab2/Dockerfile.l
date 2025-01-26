FROM gcc

COPY main.c /

RUN gcc main.c -o main.out

ENTRYPOINT ["./main.out"]
