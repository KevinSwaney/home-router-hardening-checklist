#!/usr/bin/env python3
"""Home router hardening checklist, in plain English.

The home router is the front door of the home network. If it still uses
the factory password, or remote administration is left on, anyone on the
internet can try the door. This tool walks through the five settings
that matter most and prints a plain English report with what to fix.

Usage:
    python router_checklist.py --demo     # example report, no questions
    python router_checklist.py            # interactive checklist
    python router_checklist.py --yes admin_password --yes firmware \
        --yes remote_admin_off --yes upnp_off --yes guest_network

In the --yes/--no form, each flag names a setting that is already done.
For remote_admin_off and upnp_off, "done" means the risky feature is off.

Requires Python 3.8 or later. No third party packages.
"""

import argparse
import sys

CHECKS = [
    (
        "admin_password",
        "Have you changed the router admin password from the factory default?",
        "The factory password is printed in manuals and online. Anyone who "
        "knows the router model can try it.",
    ),
    (
        "firmware",
        "Is the router firmware up to date (check the admin page or the "
        "maker's update setting)?",
        "Old firmware carries known flaws. Updates close them before they "
        "are used against you.",
    ),
    (
        "remote_admin_off",
        "Is remote administration turned OFF, so the admin page cannot be "
        "reached from the internet?",
        "Remote administration puts the login page on the public internet, "
        "where it can be attacked around the clock.",
    ),
    (
        "upnp_off",
        "Is UPnP turned OFF?",
        "UPnP lets devices open ports automatically. Attackers abuse it to "
        "open a way in without you noticing.",
    ),
    (
        "guest_network",
        "Is there a separate guest network for visitors and smart home "
        "devices, away from your main computers and files?",
        "A guest network limits the damage if a visitor device or a cheap "
        "smart gadget is compromised.",
    ),
]


def report(answers):
    out = []
    out.append("=" * 60)
    out.append("HOME ROUTER HARDENING REPORT")
    out.append("=" * 60)
    done = 0
    todo = []
    for key, question, why in CHECKS:
        if answers.get(key):
            done += 1
            out.append("[DONE] %s" % question)
        else:
            todo.append((question, why))
            out.append("[TODO] %s" % question)
            out.append("       Why it matters: %s" % why)
    out.append("-" * 60)
    out.append("Done: %d of %d" % (done, len(CHECKS)))
    if todo:
        out.append("Fix first: %s" % todo[0][0])
        out.append("How: sign in to the router admin page (usually printed "
                   "on the router label), change the setting, and save.")
    else:
        out.append("All five settings are done. Recheck after any router "
                   "reset, since a reset restores factory defaults.")
    return "\n".join(out), done


def main(argv=None):
    parser = argparse.ArgumentParser(description="Home router hardening checklist.")
    parser.add_argument("--demo", action="store_true", help="print an example report")
    parser.add_argument("--version", action="store_true", help="print version and exit")
    keys = [k for k, _, _ in CHECKS]
    parser.add_argument("--yes", dest="yes", action="append", default=[], choices=keys)
    parser.add_argument("--no", dest="no", action="append", default=[], choices=keys)
    args = parser.parse_args(argv)
    if args.version:
        print("home-router-hardening-checklist 1.0.0")
        return 0
    if args.demo:
        text, done = report({"admin_password": True, "firmware": False,
                             "remote_admin_off": True, "upnp_off": False,
                             "guest_network": True})
        print(text)
        return 0 if done == len(CHECKS) else 1
    answers = {}
    if args.yes or args.no:
        for key, _, _ in CHECKS:
            answers[key] = key in args.yes
    else:
        print("Answer yes or no for each question.")
        for key, question, _ in CHECKS:
            while True:
                reply = input(question + " (yes/no): ").strip().lower()
                if reply in ("yes", "y"):
                    answers[key] = True
                    break
                if reply in ("no", "n"):
                    answers[key] = False
                    break
                print("Please answer yes or no.")
    text, done = report(answers)
    print(text)
    return 0 if done == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
