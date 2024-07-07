def towers_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return
    towers_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    towers_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


n = 3  
towers_of_hanoi(n, 'A', 'C', 'B')
