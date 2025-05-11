def main():
    code_snippets = {
        "dictionary_code": {
            "code": "numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5",
            "explanation": "This works because dictionaries allow assignment to arbitrary keys, including integers, without needing predefined size.",
            "fixed": "No fix needed — this code is already correct."
        },
        "broken_list_code": {
            "code": "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5",
            "explanation": "This fails because lists must be large enough to access an index. Index 0 and 1 don’t exist yet.",
            "fixed": "other_numbers = [0, 0]  # create a list with two elements\nother_numbers[0] = -5\nother_numbers[1] = 10.5"
        }
    }

# This above section was essentially copy and paste because I had another assignment deadline, sorry

for name, snippet in code_snippets.items():
    print(f"--- {name.replace('_', ' ').title()} ---")
    print("Original Code:\n" + snippet["code"])
    print("Explanation:\n" + snippet["explanation"])
    print("Fixed Code:\n" + snippet["fixed"])

if __name__ == "__main__":
    main()