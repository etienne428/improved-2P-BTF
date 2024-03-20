# Simulate a distributed git environment
# etienne.mettaz@epfl.ch

from git import *
import os

PATH = "./data/"
def init_replica(name: str) -> Repo:
    return Repo.init(PATH + name, mkdir=True)

def add_file(name: int, path: str, repo: Repo):
    os.system("touch " + path + "file_" + str(name))
    repo.index.add("file_" + str(name))
    repo.index.commit("Add file_" + str(name))

if __name__=="__main__":
    os.system("rm -rf " + PATH)
    os.mkdir(PATH)
    repo_alice = init_replica("alice")
    repo_bob = init_replica("bob")

    for i in range(20):
        if (i%2 == 1):
            add_file(i, PATH + "alice/", repo_alice)
            repo_alice.commit()
        else:
            add_file(i, PATH + "bob/", repo_bob)
            repo_bob.commit()
