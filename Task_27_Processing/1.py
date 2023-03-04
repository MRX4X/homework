import multiprocessing
def chet_sum(n=10000000):
    chet_mus=0
    while n:
        n-=1
        if n%2==0:
            chet_mus += n
    print(chet_mus)
def ne_chet_sum(n=10000000):
    ne_chet_mus = 0
    while n:
        n -= 1
        if n % 2 != 0:
            ne_chet_mus+=n
    print(ne_chet_mus)

if __name__ == "__main__":

    p1=multiprocessing.Process(target=chet_sum)
    p2=multiprocessing.Process(target=ne_chet_sum)
    p1.start()
    p2.start()