#!/usr/bin/env python3
"""
Build ready-set-folder.

  _system/core/            files every package gets (START-HERE, CLAUDE/AGENTS, _system/ memory + SETUP)
  _system/niches/<name>/   one blueprint: its folders (each with a README) + _niche/ (rules, gitignore, about, emoji)

Builds (generated: never edit by hand):
  1-start-here/            the universal starter: core + all blueprints. The AI sets it up on the first "hi".
  2-ready-made/<name>/     one per blueprint, folders already made (for chat apps that can't create folders)
  dist/                    ready-set-folder.zip + <name>.zip (attached to GitHub Releases)

Usage (from the repo folder):
  python3 _system/tools/build.py            rebuild 1-start-here/ and 2-ready-made/
  python3 _system/tools/build.py --zip      rebuild and make the zips in dist/
  python3 _system/tools/build.py --check    fail if the built folders are out of date (GitHub Actions)

Only uses the Python standard library.
"""
import filecmp, json, os, re, shutil, sys, tempfile, zipfile

SYS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(SYS)
CORE = os.path.join(SYS, "core")
NICHES = os.path.join(SYS, "niches")
STARTER = os.path.join(ROOT, "1-start-here")
READY = os.path.join(ROOT, "2-ready-made")
DIST = os.path.join(ROOT, "dist")
STARTER_ZIP_TOP = "my-new-project"
MAP_DEPTH = 2

STATUS_STARTER = "⚪ **Not set up yet.** Give this folder to your AI and say \"hi\" (2 steps below)."
STATUS_READY = "🟡 **Folders ready ({name}), project not set up yet.** Give this folder to your AI and say \"hi\" (2 steps below)."


# ---------------------------------------------------------------- helpers
def config():
    with open(os.path.join(SYS, "tools", "config.json")) as f:
        cfg = json.load(f)
    with open(os.path.join(SYS, "VERSION")) as f:
        cfg["version"] = f.read().strip()
    return cfg


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)


def copy_tree(src, dst, skip=("_niche",)):
    for base, dirs, files in os.walk(src):
        dirs[:] = sorted(d for d in dirs if d not in skip)
        rel = os.path.relpath(base, src)
        for name in sorted(files):
            if name.startswith("._") or name == ".DS_Store":
                continue
            target = os.path.normpath(os.path.join(dst, rel, name))
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copyfile(os.path.join(base, name), target)


def walk_files(d):
    for base, _, files in os.walk(d):
        for f in files:
            yield os.path.join(base, f)


def names():
    return sorted(n for n in os.listdir(NICHES) if os.path.isdir(os.path.join(NICHES, n)))


def niche_extra(n, f):
    return read(os.path.join(NICHES, n, "_niche", f))


def emoji(n):
    return json.loads(niche_extra(n, "card.json"))["emoji"]


def top_folders(n):
    d = os.path.join(NICHES, n)
    return sorted(x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x)) and x != "_niche")


def describe(readme):
    """One line for a folder map: a <!-- map: ... --> comment, else the first text line."""
    s = read(readme)
    m = re.search(r"<!--\s*map:\s*(.*?)\s*-->", s)
    if m:
        return m.group(1)
    for line in s.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("<!--"):
            return line.lstrip("> ").strip()
    return ""


def folder_map(ws):
    found = []
    for base, dirs, files in os.walk(ws):
        dirs[:] = sorted(dirs)
        rel = os.path.relpath(base, ws)
        if rel == ".":
            continue
        depth = rel.count(os.sep) + 1
        if rel.startswith("_system"):  # one line for _system/, not its insides
            dirs[:] = []
            if depth > 1:
                continue
        if depth > MAP_DEPTH:
            dirs[:] = []
            continue
        if "README.md" in files:
            path = rel.replace(os.sep, "/") + "/"
            found.append((path.startswith("_"), path, describe(os.path.join(base, "README.md"))))
    rows = ["| Folder | What goes in it |", "|---|---|"]
    rows += [f"| `{p}` | {d} |" for _, p, d in sorted(found)]
    return "\n".join(rows)


def blueprint_table():
    rows = ["| Blueprint | For | Top-level folders |", "|---|---|---|"]
    for n in names():
        folders = " · ".join(f"`{f}/`" for f in top_folders(n))
        rows.append(f"| {emoji(n)} **{n}** | {niche_extra(n, 'about.md').strip()} | {folders} |")
    return "\n".join(rows)


def fill(dest, values):
    for p in walk_files(dest):
        if p.endswith(".md"):
            s = read(p)
            for k, v in values.items():
                s = s.replace(k, v)
            write(p, s)
    left = [p for p in walk_files(dest) if p.endswith(".md") and "{{" in read(p)]
    if left:
        sys.exit(f"build: unfilled {{{{…}}}} in {left}")


# ---------------------------------------------------------------- builders
def add_core_and_blueprints(dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    copy_tree(CORE, dest)
    for n in names():
        bp = os.path.join(dest, "_system", "blueprints", n)
        copy_tree(os.path.join(NICHES, n), bp)
        write(os.path.join(bp, "_blueprint", "rules.md"), niche_extra(n, "HOUSE-RULES.md"))
        write(os.path.join(bp, "_blueprint", "gitignore.txt"), niche_extra(n, "gitignore"))
        write(os.path.join(bp, "_blueprint", "about.md"), niche_extra(n, "about.md"))
    write(os.path.join(dest, "_system", "blueprints", "README.md"),
          "# _system/blueprints/\n\nFolder plans for different kinds of projects. The setup (`_system/SETUP.md`) copies one of them "
          "to the top of this folder. Each has its folders (with READMEs) and `_blueprint/` (its extra house rules, `.gitignore` lines, description).\n")


def build_starter(dest, cfg):
    add_core_and_blueprints(dest)
    write(os.path.join(dest, "README.md"),
          "# New project\n\n⚪ **This folder isn't set up yet.** Open [`START-HERE.md`](START-HERE.md): give the folder to your AI "
          "and say \"hi\". The setup replaces this file with your project card.\n")
    fill(dest, {
        "{{STATUS_LINE}}": STATUS_STARTER,
        "{{ORIGIN}}": "starter, workspace chosen at setup",
        "{{VERSION}}": cfg["version"],
        "{{REPO_URL}}": cfg["repo_url"],
        "{{BLUEPRINT_TABLE}}": blueprint_table(),
    })


def build_ready(n, dest, cfg):
    add_core_and_blueprints(dest)
    copy_tree(os.path.join(NICHES, n), dest)  # the folders, at the top
    sysd = os.path.join(dest, "_system")
    hr = os.path.join(sysd, "HOUSE-RULES.md")
    write(hr, read(hr).replace("<!-- NICHE-RULES -->", niche_extra(n, "HOUSE-RULES.md").strip()))
    gi = os.path.join(dest, ".gitignore")
    write(gi, read(gi).rstrip() + "\n\n" + niche_extra(n, "gitignore"))
    card = read(os.path.join(sysd, "PROJECT-CARD.md")).replace("**<workspace>**", f"**{n}**")
    write(os.path.join(dest, "README.md"), card)
    write(os.path.join(dest, "README.md"), card.replace("<!-- FOLDER-MAP -->", folder_map(dest)))
    fill(dest, {
        "{{STATUS_LINE}}": STATUS_READY.format(name=n),
        "{{ORIGIN}}": f"{n} workspace",
        "{{VERSION}}": cfg["version"],
        "{{REPO_URL}}": cfg["repo_url"],
        "{{BLUEPRINT_TABLE}}": blueprint_table(),
    })


def ready_readme(cfg):
    rows = []
    for n in names():
        url = f"{cfg['repo_url']}/releases/latest/download/{n}.zip"
        rows.append(f"| {emoji(n)} **[{n}]({n}/)** | {niche_extra(n, 'about.md').strip()} | [⬇ {n}.zip]({url}) |")
    return "\n".join([
        "# 2 · Ready-made workspaces",
        "",
        "Same as the starter, but **the folders are already made** for one kind of project.",
        "Use one if you already know what you need, or if your AI is a chat app (claude.ai, ChatGPT, Gemini) that can't create folders.",
        "",
        "| Workspace | For | Download |",
        "|---|---|---|",
        *rows,
        "",
        "## How to use it",
        "1. **Download** a zip, unzip it, rename the folder to your project.",
        "2. **Give it to your AI** and say **\"hi\"**. It asks a few questions about your project and fills everything in. (Details: `START-HERE.md` inside.)",
        "",
        "Not sure which one? Use the **[starter](../1-start-here/)** instead: the AI picks for you.",
        "",
        f"<sub>Generated by `_system/tools/build.py` ({cfg['version']}). Don't edit by hand.</sub>",
        "",
    ])


# ---------------------------------------------------------------- checks + zips
def same_tree(a, b):
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    if mismatch or errors:
        return False
    return all(same_tree(os.path.join(a, d), os.path.join(b, d)) for d in cmp.common_dirs)


def make_zip(src, zpath, top):
    os.makedirs(os.path.dirname(zpath), exist_ok=True)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(walk_files(src)):
            rel = os.path.relpath(p, src).replace(os.sep, "/")
            info = zipfile.ZipInfo(f"{top}/{rel}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            with open(p, "rb") as f:
                z.writestr(info, f.read())


def main():
    cfg = config()
    args = set(sys.argv[1:])
    if "--check" in args:
        bad = []
        with tempfile.TemporaryDirectory() as tmp:
            build_starter(os.path.join(tmp, "starter"), cfg)
            if not os.path.isdir(STARTER) or not same_tree(os.path.join(tmp, "starter"), STARTER):
                bad.append("1-start-here")
            for n in names():
                build_ready(n, os.path.join(tmp, n), cfg)
                if not os.path.isdir(os.path.join(READY, n)) or not same_tree(os.path.join(tmp, n), os.path.join(READY, n)):
                    bad.append(f"2-ready-made/{n}")
        rr = os.path.join(READY, "README.md")
        if not os.path.exists(rr) or read(rr) != ready_readme(cfg):
            bad.append("2-ready-made/README.md")
        if bad:
            sys.exit(f"check: out of date: {bad}. Run: python3 _system/tools/build.py")
        print(f"check: starter + {len(names())} ready-made workspaces up to date ({cfg['version']})")
        return
    build_starter(STARTER, cfg)
    print("built 1-start-here/")
    for n in names():
        build_ready(n, os.path.join(READY, n), cfg)
        print(f"built 2-ready-made/{n}")
    write(os.path.join(READY, "README.md"), ready_readme(cfg))
    if "--zip" in args:
        make_zip(STARTER, os.path.join(DIST, "ready-set-folder.zip"), STARTER_ZIP_TOP)
        print("zipped dist/ready-set-folder.zip")
        for n in names():
            make_zip(os.path.join(READY, n), os.path.join(DIST, f"{n}.zip"), n)
            print(f"zipped dist/{n}.zip")


if __name__ == "__main__":
    main()
