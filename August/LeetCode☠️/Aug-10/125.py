s = "A man, a plan, a canal: Panama"

clean_s = s.lower()
clean_s = clean_s.replace(" ", "")
clean_s = clean_s.replace(",", "")
clean_s = clean_s.replace(":", "")
clean_s = clean_s.replace(".", "")
clean_s = clean_s.replace("!", "")
clean_s = clean_s.replace("'", "")
clean_s = clean_s.replace('"', "")

rev = clean_s[::-1]

print(rev == clean_s)