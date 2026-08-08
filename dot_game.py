
# Initialize variables
vocabulary = []
inform_learner = "The following are words present in your vocabulary:"


# vocab_meaning_one = dictionary[0]
# vocab_meaning_two = dictionary[1]
# vocab_meaning_three = dictionary[2]
# vocab_meaning_four = dictionary[3]
# vocab_meaning_five = dictionary[4]


comprehension_defined = "means to understand something fully."






print("=============== LEARNERS' VOCABULARY COLLECTOR ================\n")

print("Welcome to learners' vocabulary collection. Choose an option from the menu to proceed. \n")

while True:
        print("=========== MENU ==============")
        print("1. Start Vocabulary Collection")
        print("2. View Vocabulary Collection")
        print("3. Close Vocabulary")
        print("==============================")

        menu_choice = input("Select menu number: ")
        print(f"\n{inform_learner} \nType 'done' when ready to save the collection.\n")


        if menu_choice == "1":
            
                first_learner_choice = input("Type the word to add to your vocabulary: ")
                if first_learner_choice == "done":
                    print("Vocabulary collection saved successfully.")
                    continue
                else:
                        vocabulary.append(first_learner_choice)
                        print(f"'{first_learner_choice}' has been added to your vocabulary.\n")

                second_learner_choice = input("Type the word to add to your vocabulary: ")
                if second_learner_choice == "done":
                    print("Vocabulary collection saved successfully.")
                    continue
                else:
                    vocabulary.append(second_learner_choice)
                    print(f"'{second_learner_choice}' has been added to your vocabulary.\n")

                third_learner_choice = input("Type the word to add to your vocabulary: ")
                if third_learner_choice == "done":
                    print("Vocabulary collection saved successfully.")
                    continue
                else:
                    vocabulary.append(third_learner_choice)
                    print(f"'{third_learner_choice}' has been added to your vocabulary.\n")

                fourth_learner_choice = input("Type the word to add to your vocabulary: ")
                if fourth_learner_choice == "done":
                    print("Vocabulary collection saved successfully.")
                    continue
                else:
                    vocabulary.append(fourth_learner_choice)
                    print(f"'{fourth_learner_choice}' has been added to your vocabulary.\n")

                fifth_learner_choice = input("Type the word to add to your vocabulary: ")
                if fifth_learner_choice == "done":
                    print("Vocabulary collection saved successfully.")
                    continue
                else:
                    vocabulary.append(fifth_learner_choice)
                    print(f"'{fifth_learner_choice}' has been added to your vocabulary.\n")  

        if menu_choice == "2":
            if len(vocabulary) == 0:
                print("Your vocabulary is empty. Add words.\n")
                continue

        else:
            total_vocab = len(vocabulary)
            print(f"\nTotal number of words in your vocabulary are: {total_vocab}")


    
        # for vocab in vocabulary:
        # if vocabulary[0] == vocab_meaning_one:
            print(f"{vocabulary}\n")


        if menu_choice == "3":
            break
        else:
            continue