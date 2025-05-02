# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

# Collection of authors and year of death
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

# Print formatted statements
for author, date in authors.items():
    print(f"{author} died in {date}.")  # Full sentence

print()  # Blank line for separation

# Print name and year pairs
for author, date in authors.items():
    print(f"{author}, {date}")
