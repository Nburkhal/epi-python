#!/usr/bin/env python3

def hIndex(citations):
    citations.sort(reverse=True)
    return max([min(k+1, v) for k,v in enumerate(citations)]) if citations else 0

if __name__ == '__main__':
    cites = [1, 4, 1, 4, 2, 1, 3, 5, 6]

    print(hIndex(cites))
