import pathlib

p = pathlib.Path(".")

files = [x for x in p.iterdir() if (x.as_posix().split(".")[-1] == "vcf")]

for file in files:
    with open(file.as_posix(), "r") as input_file:
        content = input_file.read()
        with open("Contacts.vcf", "a") as output_file:
            output_file.write(content)

