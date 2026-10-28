# Home Router Hardening Checklist

## The business risk first

For a home worker, the home router is the office front door. It guards every work laptop, every video call, and every file that passes through the house. If it still uses the factory password, or its admin page is reachable from the internet, an attacker does not need to trick anyone. They can simply try the door. The cost shows up as a compromised home network, stolen credentials, and an incident that started nowhere near the office.

This checklist covers the five settings that matter most, in plain English, with a report that says exactly what to fix first.

## What it checks

- **Admin password changed:** the factory password is public knowledge. Change it.
- **Firmware up to date:** old firmware carries known flaws. Updates close them.
- **Remote admin off:** the admin page must not be reachable from the internet.
- **UPnP off:** automatic port opening is abused to open a way in unnoticed.
- **Guest network on:** visitors and smart home devices stay separate from main computers and files.

## Run it

```bash
python router_checklist.py --demo
python router_checklist.py
```

Or pass answers directly:

```bash
python router_checklist.py --yes admin_password --yes remote_admin_off
```

## One warning that matters

A router reset restores factory defaults. After any reset, run this checklist again before reconnecting work devices.

## Requirements

Python 3.8 or later. No third party packages. This tool asks questions and prints a report. It does not log in to your router or change settings itself, so your credentials never leave your hands.

## Author

Kevin Swaney, Principal Cybersecurity Engineer. More at [kevintswaney.com](https://kevintswaney.com).
