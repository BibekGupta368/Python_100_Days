def calculate_love_score(name1, name2):
    # Combine names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count occurrences for letters in "TRUE"
    t_count = combined_names.count("t")
    r_count = combined_names.count("r")
    u_count = combined_names.count("u")
    e_count = combined_names.count("e")
    true_total = t_count + r_count + u_count + e_count
    
    print(f"T occurs {t_count} times")
    print(f"R occurs {r_count} times")
    print(f"U occurs {u_count} times")
    print(f"E occurs {e_count} times")
    print(f"True Total = {true_total}")
    
    # Count occurrences for letters in "LOVE"
    l_count = combined_names.count("l")
    o_count = combined_names.count("o")
    v_count = combined_names.count("v")
    e_count_love = combined_names.count("e")
    love_total = l_count + o_count + v_count + e_count_love
    
    print(f"L occurs {l_count} times")
    print(f"O occurs {o_count} times")
    print(f"V occurs {v_count} times")
    print(f"E occurs {e_count_love} times")
    print(f"Love Total = {love_total}")
    
    # Combine the two totals to get the love score
    love_score = int(str(true_total) + str(love_total)) # or love_score = f"{true_total}{love_total}"

    print(f"\nLove score ={love_score}")

name1 = input("Enter your name:\n")
name2 = input("Enter your partner name:\n")
calculate_love_score(name1, name2)