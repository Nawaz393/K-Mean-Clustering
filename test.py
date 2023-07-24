from Cluster import clustering
from Helpers import Question


def main():
    question,ks=Question()
    result=clustering(question,ks)
    print(result)
if __name__ == "__main__":
    main()



