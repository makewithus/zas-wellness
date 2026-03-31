import codecs

test3_path = r"c:\Downloaded Web Sites\fitcore-ttm.webflow.io\test3.html"
test4_path = r"c:\Downloaded Web Sites\fitcore-ttm.webflow.io\test4.html"

with codecs.open(test3_path, "r", "utf-8") as f:
    test3_lines = f.readlines()

# In test3.html, the Anthem GSAP hero is lines 362 through 778 (indexes 361 to 778 exclusive, i.e. 361:778)
anthem_hero_lines = test3_lines[361:778]

with codecs.open(test4_path, "r", "utf-8") as f:
    test4_lines = f.readlines()

# In test4.html, the Premium hero section is lines 362 through 725 (indexes 361 to 725 exclusive, i.e. 361:725)
new_test4_lines = test4_lines[:361] + anthem_hero_lines + test4_lines[725:]

with codecs.open(test4_path, "w", "utf-8") as f:
    f.writelines(new_test4_lines)

print("Hero section restored successfully to ZAS Wellness from test3.html.")
