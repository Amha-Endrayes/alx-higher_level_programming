#!/usr/bin/python3
"""
Holberton School Interview Question:
A Module to list the last 10 commits of a
git repo.
Usage: >> $  ./100-github_commits.py @arg1 @arg2
    @arg1: repository name
    @arg2: owner name
"""
import sys
import requests


def apidata():
    """pharses repo detail fromuser input and lists last 10 commits"""
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    result = requests.get(url)
    try:
        r = result.json()
        for i in range(10):
            print("{}: {}".format(r[i]["sha"],
                                  r[i]["commit"]["author"]["name"]))
    except IndexError:
        pass


if __name__ == "__main__":
    apidata()
