import subprocess

# Define the scripts to run
scripts = [
    "data_preparation.py",
    "inferential_statistics.py",
    "probability_race_part.py"
]

# Run each script
for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)
    print(f"Finished {script}.\n")

print("All scripts have been successfully executed.")
