#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(dna_string1: str, dna_string2:str) -> tuple:
    positions = []
    len_sub = len(dna_string2)
    for i in range(len(dna_string1) - len_sub + 1):
        if dna_string1[i:i+len_sub] == dna_string2:
            positions.append(i + 1)
    return tuple(positions)

def validated_dna_input(prompt: str, min_len: int = 0, max_len: int = 0, exact_len: int = 0) -> str:
    while True:
        dna = input(prompt).upper().strip()

        if not all(c in 'ATCG' for c in dna):
            print ("Invalid characters. Only A,T C, G is allowed.")
            continue
        if exact_len:
            if len(dna) != exact_len:
                print(f"Must be exactly {exact_len} characters.")
                continue
        else:
            if len(dna) <= min_len:
                print(f"Must be longer than {min_len} characters.")
                continue
            if len(dna) > max_len: 
                print(f"Must be {max_len} characters or fewer.")
                continue

        return dna
def test_config() -> bool:
    return True


         