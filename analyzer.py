info = 0
error = 0
warning = 0

with open("logs.txt", "r") as file:
    for line in file:
        if line.startswith("INFO"):
            info += 1
        elif line.startswith("ERROR"):
            error += 1
        elif line.startswith("WARNING"):
            warning += 1

with open("report.txt", "w") as report:
    report.write("Log Summary Report\n")
    report.write("------------------\n")
    report.write(f"INFO: {info}\n")
    report.write(f"ERROR: {error}\n")
    report.write(f"WARNING: {warning}\n")

print("Report Generated Successfully")
