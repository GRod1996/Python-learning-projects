# CS 1350 - Homework 7, Problem 1: Security Log Splitter and Status Report
LEVELS = ["INFO", "WARNING", "ERROR"]

def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        machines: dict mapping machine name -> log file name

    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {}

    # Mode "w" creates the output files fresh on every run
    with open("info.log", "w") as info_out, \
         open("warning.log", "w") as warning_out, \
         open("error.log", "w") as error_out:
        outputs = {"INFO": info_out, "WARNING": warning_out, "ERROR": error_out}

        for machine, log_file in machines.items():
            counts[machine] = {"INFO": 0, "WARNING": 0, "ERROR": 0}

            with open(log_file, "r") as log:
                for line in log:
                    line = line.strip()
                    if line == "":
                        continue  # skip blank lines

                    for level in LEVELS:
                        if f"[{level}]" in line:
                            outputs[level].write(f"{machine} | {line}\n")
                            counts[machine][level] += 1
                            break

    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("SECURITY LOG REPORT")
    print("=" * 40)

    totals = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for machine, levels in counts.items():
        info = levels["INFO"]
        warning = levels["WARNING"]
        error = levels["ERROR"]
        entries = info + warning + error

        if error >= 2:
            status = "CRITICAL"
        elif error >= 1 or warning >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"

        print(f"{machine}: {entries} entries | INFO {info} | WARNING {warning} "
              f"| ERROR {error} | Status: {status}")

        for level in LEVELS:
            totals[level] += levels[level]

    print("-" * 40)
    total_entries = sum(totals.values())
    print(f"Total: {total_entries} entries | INFO {totals['INFO']} "
          f"| WARNING {totals['WARNING']} | ERROR {totals['ERROR']}")

    print(f"Errors (see {error_file}):")
    with open(error_file, "r") as f:
        for line in f:
            print("  " + line.rstrip("\n"))


# Test cases
with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
print(counts)
# {'server_a': {'INFO': 3, 'WARNING': 2, 'ERROR': 1}, 'server_b': {'INFO': 3, 'WARNING': 1, 'ERROR': 2}}

with open("warning.log", "r") as f:
    print(f.read())
# server_a | 2026-10-05 08:03:45 [WARNING] Failed login attempt for user root
# server_a | 2026-10-05 08:03:59 [WARNING] Failed login attempt for user root
# server_b | 2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted

print_report(counts)
# SECURITY LOG REPORT
# ========================================
# server_a: 6 entries | INFO 3 | WARNING 2 | ERROR 1 | Status: NEEDS ATTENTION
# server_b: 6 entries | INFO 3 | WARNING 1 | ERROR 2 | Status: CRITICAL
# ----------------------------------------
# Total: 12 entries | INFO 6 | WARNING 3 | ERROR 3
# Errors (see error.log):
#   server_a | 2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures
#   server_b | 2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start
#   server_b | 2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22

# CS 1350 - Homework 7, Problem 2: Incident Tracker

import json
import pickle
import os


def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    incidents = []

    with open(csv_file, "r") as f:
        f.readline()  # skip the header line
        for line in f:
            line = line.strip()
            if line == "":
                continue

            incident_id, machine, severity, description = line.split(",")
            incidents.append({
                "id": int(incident_id),
                "machine": machine,
                "severity": severity,
                "description": description,
            })

    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    by_machine = {}
    by_severity = {}
    high_ids = []

    for incident in incidents:
        machine = incident["machine"]
        severity = incident["severity"]

        by_machine[machine] = by_machine.get(machine, 0) + 1
        by_severity[severity] = by_severity.get(severity, 0) + 1

        if severity == "high":
            high_ids.append(incident["id"])

    summary = {
        "total": len(incidents),
        "by_machine": by_machine,
        "by_severity": by_severity,
        "high_ids": high_ids,
    }

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)

    return summary


def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    os.makedirs(folder, exist_ok=True)

    # Whole list -> pickle (binary mode)
    with open(os.path.join(folder, "incidents.pkl"), "wb") as f:
        pickle.dump(incidents, f)

    # Group incidents by machine
    per_machine = {}
    for incident in incidents:
        per_machine.setdefault(incident["machine"], []).append(incident)

    # One JSON file per machine
    for machine, machine_incidents in per_machine.items():
        with open(os.path.join(folder, f"{machine}.json"), "w") as f:
            json.dump(machine_incidents, f, indent=2)

    return sorted(os.listdir(folder))


def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(os.path.join(folder, "incidents.pkl"), "rb") as f:
        return pickle.load(f)


# Test cases
with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")

incidents = load_incidents("incidents.csv")
print(len(incidents))
# 5
print(incidents[0])
# {'id': 1, 'machine': 'server_a', 'severity': 'high', 'description': 'Account root locked'}

summary = save_summary(incidents, "summary.json")
print(summary)
# {'total': 5, 'by_machine': {'server_a': 2, 'server_b': 3},
# 'by_severity': {'high': 3, 'low': 1, 'medium': 1}, 'high_ids': [1, 2, 5]}

with open("summary.json", "r") as f:
    print(json.load(f) == summary)
# True

print(archive(incidents, "archive"))
# ['incidents.pkl', 'server_a.json', 'server_b.json']

with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])
# [1, 4]

restored = load_archive("archive")
print(restored == incidents)
# True

# CS 1350 - Homework 7, Problem 3 (Bonus): Workspace Organizer and Backup System

import os
import shutil

# Extension -> subfolder; anything not listed goes to "other"
SUBFOLDERS = {
    ".log": "logs",
    ".csv": "data",
    ".json": "data",
    ".pkl": "pickles",
}


def organize(folder):
    """Move files into logs/, data/, pickles/, other/ by extension."""
    moved = {"logs": [], "data": [], "pickles": [], "other": []}

    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue  # leave existing subfolders alone

        extension = os.path.splitext(name)[1].lower()
        subfolder = SUBFOLDERS.get(extension, "other")

        destination = os.path.join(folder, subfolder)
        os.makedirs(destination, exist_ok=True)
        shutil.move(path, os.path.join(destination, name))
        moved[subfolder].append(name)

    for subfolder in moved:
        moved[subfolder].sort()

    return moved


def create_backup(source_dir, backup_root, label):
    """Copy source_dir to backup_root/backup_<label>; return the new path."""
    os.makedirs(backup_root, exist_ok=True)
    backup_dir = os.path.join(backup_root, f"backup_{label}")
    shutil.copytree(source_dir, backup_dir)
    return backup_dir


def verify_backup(source_dir, backup_dir):
    """Return True if every file under source_dir is in backup_dir with the same size."""
    for current_dir, subdirs, files in os.walk(source_dir):
        for name in files:
            source_path = os.path.join(current_dir, name)
            relative = os.path.relpath(source_path, source_dir)
            backup_path = os.path.join(backup_dir, relative)

            if not os.path.isfile(backup_path):
                return False
            if os.path.getsize(source_path) != os.path.getsize(backup_path):
                return False

    return True


def cleanup_old_backups(backup_root, keep):
    """Delete all but the newest `keep` backups; return sorted names deleted."""
    backups = sorted(
        name for name in os.listdir(backup_root)
        if os.path.isdir(os.path.join(backup_root, name))
    )

    # Oldest come first, so everything except the last `keep` gets deleted
    to_delete = backups[:max(len(backups) - keep, 0)]

    for name in to_delete:
        shutil.rmtree(os.path.join(backup_root, name))

    return to_delete


# Test cases
# Start clean so the test can be re-run
for old in ["workspace", "backups"]:
    if os.path.exists(old):
        shutil.rmtree(old)

os.mkdir("workspace")
for name in ["a.log", "b.log", "incidents.csv", "summary.json", "incidents.pkl", "notes.txt"]:
    with open(os.path.join("workspace", name), "w") as f:
        f.write(f"Test file: {name}\n")

print(organize("workspace"))
# {'logs': ['a.log', 'b.log'], 'data': ['incidents.csv', 'summary.json'],
# 'pickles': ['incidents.pkl'], 'other': ['notes.txt']}

print(sorted(os.listdir("workspace")))
# ['data', 'logs', 'other', 'pickles']

for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:
    path = create_backup("workspace", "backups", label)
    print(os.path.basename(path), verify_backup("workspace", path))
# backup_2026-10-01 True
# backup_2026-10-02 True
# backup_2026-10-03 True

# Damage one backup: verification must now fail
os.remove(os.path.join("backups", "backup_2026-10-03", "logs", "a.log"))
print(verify_backup("workspace", os.path.join("backups", "backup_2026-10-03")))
# False

print(cleanup_old_backups("backups", 2))
# ['backup_2026-10-01']

print(sorted(os.listdir("backups")))
# ['backup_2026-10-02', 'backup_2026-10-03']
