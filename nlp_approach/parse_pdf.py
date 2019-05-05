# %%
import subprocess
import os
import re



# %% Convert PDF to text using pdftotext
in_dir = "data/transcripts"
out_dir = "data/transcripts"
path = os.path.join(os.getcwd(), in_dir)
out_path = os.path.join(os.getcwd(), out_dir)

#%%
for file in os.listdir(path):
    if file.endswith(".pdf"):
        print(f"Converting {file}")
        subprocess.run(
            ["pdftotext",
             "-enc", "UTF-8", "-nopgbrk",
             os.path.join(path, file),
             os.path.join(out_path, file.replace(".pdf", ".txt"))
             ])

# %% Parse text into statements using regex
# All nominee statements are preceded by their title+capitalized name, and are
# followed either by the name of the senator/chairperson who replies to them
# or the string [The prepared statement follows:]
names = {
    "AFortas": "fortas",
    "AJGoldberg": "goldberg",
    "AMKennedy": "kennedy",
    "AScalia": "scalia",
    "BRWhite": "white",
    "DHSouter": "souter",
    "EKagan": "kagan",
    "EWarren": "warren",
    "HABlackmun": "blackmun",
    "JGRoberts": "roberts",
    "JPStevens": "stevens",
    "LFPowell": "powell",
    "NMGorsuch": "gorsuch",
    "RBGinsburg": "ginsburg",
    "SDOConnor": "o'connor",
    "SAAlito": "alito",
    "SGBreyer": "breyer",
    "SSotomayor": "sotomayor",
    "TMarshall": "marshall",
    "WHRehnquist": "rehnquist"
}

# for file in os.listdir(path):
#     if file.endswith(".txt"):

file = "AScalia.pdf"
# Capitalize name based on filename. Filenames contain _chief
# to denote that this is theirsecond confirmation hearing, for chief justice
# but need to remove this in order to match the transcript
# Also add apostrophe to oconnor
name = names[file.split(".")[0].replace("_Chief", "")].upper()
print(f"Extracting utterances from {file} for {name}")


regex = ""
# Look behinds in python need to be fixed length, so in order to emulate
# "|" in lookbehinds, we just create a union of regexes, one of each possible
# lookbehind
for i, prefix in enumerate(["Judge", "Ms.", "Mr.", "Mrs.", "Justice"]):
    if i != 0:
        regex += "|"
    regex += f"((?<=({prefix} {name}(\. )))" + \
        "(.*?)(?=(((Senator|Chairman) ([A-Z]|'){2,}|\[The prepared|The CHAIRMAN|\[The initial questionnaire))))"

print(f"Using regex {regex}")
transcript = open(os.path.join(path, file), "r")
utterance_dir = "utterances"
# Remove page headers that start with VerDate, as well as page numbers and empty lines
len_text = len(text)
text = ""

for line in transcript.readlines():
    line = line.replace("\r", "").replace("\n", "")
    if not line.startswith("VerDate") and not line.isdigit():
        text += line

utterances = [match.group(0) for match in re.finditer(regex, text)]
print(f"Got {count} utterances from {len_text} lines")
with open(os.path.join(path, utterance_dir, file), "w") as utterance_file:
    utterance_file.write("\n\n".join(utterances))
