names = ["  krisha", "Riya  ", "ANKIT", "krisha", "  ankit  ", "Megha"]

cleaned_names = []
for name in names:
    clean_name = name.strip().title()
    if clean_name not in cleaned_names:
        cleaned_names.append(clean_name)

print("Original names:", names)
print("Cleaned names:", cleaned_names)