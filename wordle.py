import matplotlib.pyplot as plt

# Original Wordle word list
with open("Wordle.txt", "r") as wordle_file:
    data = wordle_file.read()
    words = data.split(",")

# Getting counts of letters
general = dict()
first = dict()
second = dict()
third = dict()
fourth = dict()
fifth = dict()

for word in words:
    letters = list(word)
    for i in range(5):
        if i == 0:
            first[letters[i]] = first.get(letters[i], 0) + 1
        elif i == 1:
            second[letters[i]] = second.get(letters[i], 0) + 1
        elif i == 2:
            third[letters[i]] = third.get(letters[i], 0) + 1
        elif i == 3:
            fourth[letters[i]] = fourth.get(letters[i], 0) + 1
        else:
            fifth[letters[i]] = fifth.get(letters[i], 0) + 1

        general[letters[i]] = general.get(letters[i], 0) + 1

# Sorting the dictionary by count
general = dict(sorted(general.items(), key=lambda item: item[1], reverse=True)[:10])
first = dict(sorted(first.items(), key=lambda item: item[1], reverse=True)[:10])
second = dict(sorted(second.items(), key=lambda item: item[1], reverse=True)[:10])
third = dict(sorted(third.items(), key=lambda item: item[1], reverse=True)[:10])
fourth = dict(sorted(fourth.items(), key=lambda item: item[1], reverse=True)[:10])
fifth = dict(sorted(fifth.items(), key=lambda item: item[1], reverse=True)[:10])

# Creating visualizations
gen_letters = list(general.keys())
gen_values = list(general.values())

fir_letters = list(first.keys())
fir_values = list(first.values())

sec_letters = list(second.keys())
sec_values = list(second.values())

thi_letters = list(third.keys())
thi_values = list(third.values())

for_letters = list(fourth.keys())
for_values = list(fourth.values())

fif_letters = list(fifth.keys())
fif_values = list(fifth.values())

plt.subplot(3,2,6)
plt.bar(gen_letters, gen_values)
plt.xlabel("Letters")
plt.ylabel("Count")
plt.title("Top 10 Letters")

plt.subplot(3,2,1)
plt.bar(fir_letters, fir_values)
plt.xlabel("Letters")
plt.ylabel("Count")
plt.title("Top 10 First Letters")

plt.subplot(3,2,2)
plt.bar(sec_letters, sec_values)
plt.xlabel("Letters")
plt.ylabel("Count")
plt.title("Top 10 Second Letters")

plt.subplot(3,2,3)
plt.bar(thi_letters, thi_values)
plt.xlabel("Letters")
plt.ylabel("Count")
plt.title("Top 10 Third Letters")

plt.subplot(3,2,4)
plt.bar(for_letters, for_values)
plt.xlabel("Letters")
plt.ylabel("Count")
plt.title("Top 10 Fourth Letters")

plt.subplot(3,2,5)
plt.bar(fif_letters, fif_values)
plt.xlabel("Letters")
plt.ylabel("Count")
plt.title("Top 10 Fifth Letters")

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()