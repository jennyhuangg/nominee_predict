# %%
import subprocess
import os
import re

# %% Convert PDF to text using pdftotext
in_dir = "transcripts"
out_dir = "transcripts"
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

for file in os.listdir(path):
    if file.endswith(".txt"):
        print(f"Extracting utterances from {file}")
        # Capitalize name based on filename. Filenames contain _chief
        # to denote that this is theirsecond confirmation hearing, for chief justice
        # but need to remove this in order to match the transcript
        # Also add apostrophe to oconnor
        name = file.split(".")[0].replace("_chief", "").replace("oconnor", "o'connor").upper()

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
        transcript = open(os.path.join(path, file))

        utterance_dir = "utterances"
        # Remove page headers that start with VerDate, as well as page numbers and empty lines
        text = ""
        for line in transcript:
            line = line.replace("\r", "").replace("\n", "")
            if not line.startswith("VerDate") and not line.isdigit():
                text += line

        utterances = [match.group(0) for match in re.finditer(regex, text)]

        with open(os.path.join(path, utterance_dir, file), "w") as utterance_file:
            utterance_file.write("\n\n".join(utterances))
