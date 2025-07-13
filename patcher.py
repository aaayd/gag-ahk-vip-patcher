from pathlib import Path

source = Path(__file__).with_name("Main.ahk")
output = source.with_name("Main-patched.ahk")

if not source.exists():
    print(f"Error: {source} not found")
    exit(1)

targets = {
    "if (VerifyUser(rbUser)) {",
    "if (fff(rbUser)) {"
}
inputbox_line = "InputBox, rbUser, Premium Access, Please enter your Roblox username:"

with source.open(encoding="utf-8") as src, output.open("w", encoding="utf-8") as out:
    for line in src:
        stripped = line.strip()

        if stripped in targets:
            out.write(f"; {line}")
            out.write("if (True) {\n")
        elif stripped == inputbox_line:
            out.write(f"; {line}")
        else:
            out.write(line)

print(f"✅ Patched file written to {output}")
