from RandomSetCollection import RandomSetCollection as RSC
from CSVSetCollection import CSVSetCollection as CSC


def f(i):
    if i == 1:
        for n in range(3, 10):
            C = RSC(n)
            print("----------------------------------------------------")
            print("n = {}".format(n))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("My Collection:")
            print(C)
            print("==============================")
            print("My Covering:")
            D = C.covering()
            print(D)
    if i == 2:
        for n in range(10):
            C = RSC(n)
            print("----------------------------------------------------")
            print("n = {}".format(n))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("My Collection:")
            print(C)
            print("############")
            C.toCSV("collection_{}".format(n))
            E = CSC("collection_{}.csv".format(n))
            print("CSV Collection:")
            print(E)




if __name__ == '__main__':
    f(1)


