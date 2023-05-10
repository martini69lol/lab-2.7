#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"c", "e", "h", "n"}
    b = {"e", "f", "k", "n", "x"}
    c = {"b", "c", "h", "p", "r", "s"}
    d = {"d", "e", "g"}

    # а является подмножеством множества b и это все пересекается с d
    x = (a.difference(b)).intersection(c.union(d))
    print(f"x = {x}")

    # Найдем дополнения множеств
    ab = u.difference(b)

    y = (a.intersection(ab)).union(c.intersection(d))
    print(f"y = {y}")
