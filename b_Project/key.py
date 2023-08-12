
from code_code.key_script import Key

key = Key()

# sample masks

mask1 = [None, None, None, 3, 2, 3, None, None, None, None, 3, 2, 0, None, None, None, 4, None, None, None, None, None, 0, None, None, None, None, 4, None, 2, None, None, None, None, None, 1, None, None, 7, 0, None, None, None, None]
mask2 = [None, 2, 0, None, None, None, None, 0, 1, 8, None, None, None, None, None, None, None, None, 2, 0, None, None, None, 2, 2, None, 1, None, 2, None, 2, None, None, None, 0, None, None, None, None, None, 1, None, 2, 5]
mask3 = [0, 0, None, None, None, None, None, None, None, None, None, 4, 0, None, 7, None, None, None, None, None, None, None, None, None, None, 0, 5, None, 4, None, 3, 1, 0, None, None, None, None, None, 1, None, None, None, None, None]
mask4 = [1, 2, None, None, 2, None, None, None, None, None, None, None, None, None, None, 3, None, None, 5, None, None, None, None, None, None, None, None, None, 0, None, None, None, None, 2, None, None, 7, 1, None, None, None, None, None, 1]
mask5 = [4, 3, None, 1, 0, 2, None, None, 0, None, 8, None, None, 6, None, 2, 1, None, 4, None, 6, None, 0, None, None, None, None, None, None, None, None, None, None, 3, 0, None, None, 0, 1, 3, None, 0, None, None]
mask6 = [0, None, None, 4, None, None, None, None, None, None, 6, 3, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None, 4, None, None, None, None, None, None, None, None, None, None, 6, None, None, None, 1, 3]
mask7 = [2, 1, 0, None, None, None, None, None, None, 11, None, None, None, 1, None, None, None, None, None, 2, 5, None, None, None, 4, 0, None, None, None, 8, 2, None, 2, None, None, None, None, None, None, 0, None, None, None, None]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
mask8 = [None, None, None, None, None, None, None, None, 5, None, 6, None, None, None, 2, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0, None, 6, None, None, 6, None, None, None, 0]
mask9 = [None, 3, None, 6, 1, None, None, None, 7, 9, 6, None, None, None, None, None, 7, None, None, None, None, None, None, 5, None, None, None, 3, 3, None, None, None, 0, 3, 0, 2, 7, None, 3, None, None, None, None, None]
mask10 = [None, 3, None, None, None, None, None, None, None, None, 3, None, None, None, None, 2, 6, None, None, None, 2, 2, None, None, None, None, None, 1, None, None, None, 5, None, 3, None, None, None, 2, 3, None, None, None, None, None]
mask11 = [None, None, 1, 5, None, None, None, None, 3, None, None, None, None, 1, 4, 0, None, None, None, None, None, 2, 0, 1, None, None, None, None, None, None, None, None, None, 2, 0, None, None, None, None, None, None, None, None, None]
mask12 = [1, 0, 1, 5, None, None, 0, 7, 6, None, 9, None, None, None, None, None, 6, None, 5, None, 5, 8, None, None, None, None, None, None, None, None, 2, None, 1, None, 0, None, 6, 2, 5, 6, None, None, None, 5]
mask13 = [1, 0, 0, None, 1, 0, None, 2, None, 0, None, None, 0, None, 2, None, 0, None, None, 0, 5, None, None, 2, None, None, 0, 0, None, None, None, None, None, 0, None, None, 0, None, None, None, 2, None, None, 4]
mask14 = [4, None, 0, None, 1, None, None, None, None, None, None, None, 0, None, None, 4, None, None, None, None, None, None, None, 1, None, None, 1, None, None, 2, None, 2, None, None, 0, 1, None, None, None, 1, 3, None, 0, None]
mask15 = [None, None, None, None, 1, None, None, None, None, None, 2, None, None, None, None, None, 1, None, 2, 2, None, None, None, None, None, None, None, 3, 1, None, None, None, None, None, 0, None, None, None, None, 1, 0, None, 1, 4]
mask16 = [None, None, 1, 1, 0, None, None, None, None, None, None, 0, None, 5, 4, None, None, None, 1, 4, 1, None, 0, None, 2, None, None, None, None, None, 1, None, None, None, 0, None, None, 2, None, None, None, None, 1, None]
mask17 = [None, 1, None, 2, None, None, None, None, None, None, None, None, 2, None, 1, None, None, 1, None, None, 1, None, 0, 3, None, 0, None, None, None, 6, None, 1, None, None, None, None, 1, None, 3, 5, None, None, None, 2]
mask18 = [0, None, None, None, None, 3, None, None, 5, None, 0, 2, 1, None, None, None, None, 1, None, None, 3, None, None, 0, None, 0, None, 1, 5, None, None, 3, None, None, 0, None, None, 0, 1, None, None, None, None, 5]
mask19 = [None, 0, None, 3, 1, None, 5, None, None, 9, None, None, 1, None, None, 1, None, 4, 4, None, None, None, None, None, 4, None, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, 0, 4]
mask20 = [None, None, None, None, None, None, None, None, 3, 10, 6, None, None, None, 4, None, 3, None, None, None, None, 2, 0, None, None, None, 1, None, None, None, 2, 1, 2, None, None, None, None, None, 5, 1, None, None, None, None]


key.mapping("pusty_plik.txt", mask1)

