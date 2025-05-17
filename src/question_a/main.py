from question_a import get_most_likely_ancestor_consensus, validated_dna_input

def main():
    print("\nDna Substring Position Finder")

    while True:
        main_dna = validated_dna_input(
            "Enter main DNA sequence (9-16 characters): ",
            min_len = 8,
            max_len = 17
        )
        sub_dna = validated_dna_input(
            "Enter 4-character substring to find: ",
            exact_len = 4
        )

        positions = get_most_likely_ancestor_consensus(main_dna, sub_dna)

        if positions:
            print("Found at positions:", ' '.join(map(str, positions)))
        else:
            print("Substring not found in main DNA.")

        if input("\Check another sequence (y/n): ").lower() != 'y':
            print("Program ended.")
            break

if __name__ == "__main__":
    main()
