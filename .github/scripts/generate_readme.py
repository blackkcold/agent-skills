#!/usr/bin/env python3
import base64
import json
import os
import sys
import urllib.request
from html import escape

API = "https://api.github.com"
ROOT_MARKER = "__ROOT__"


def api_get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def api_get_b64(url):
    data = api_get(url)
    raw = data.get("content") or ""
    return base64.b64decode(raw).decode("utf-8", "replace") if raw else ""


def load_config(root):
    path = os.path.join(root, "skills.yml")
    owner, repos = "blackkcold", []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("owner:"):
                owner = line.split(":", 1)[1].strip()
            elif line.startswith("- "):
                repos.append(line[2:].strip())
    return owner, repos


def scan_skill_dirs(owner, repo, branch):
    tree = api_get(f"{API}/repos/{owner}/{repo}/git/trees/{branch}?recursive=1")
    dirs = set()
    for item in tree.get("tree", []):
        if item.get("type") == "blob" and item.get("path", "").endswith("SKILL.md"):
            parent = item["path"].rsplit("/SKILL.md", 1)[0]
            dirs.add(parent if parent else ROOT_MARKER)
    return sorted(dirs)


def readme_first_line(owner, repo, branch):
    try:
        text = api_get_b64(f"{API}/repos/{owner}/{repo}/readme?ref={branch}")
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("!["):
                continue
            return line[:120]
    except Exception:
        pass
    return ""


def deploy_block(owner, name, repo, skill_dir):
    clone_dir = f"/tmp/{repo}-install"
    src = clone_dir + (f"/{skill_dir}" if skill_dir else "")
    targets = {
        "通用 (任意 harness，下载到当前目录)": f"./{name}",
        "OpenCode": f"~/.config/opencode/skills/{name}",
        "Claude Code": f"~/.claude/skills/{name}",
        "Codex CLI": f"~/.codex/skills/{name}",
    }
    parts = ["<details>", f"<summary><b>{escape(name)}</b> · 一键部署</summary>", ""]
    for title, target in targets.items():
        parts += [
            f"**{title}**",
            "",
            "```bash",
            f"git clone --depth 1 https://github.com/{owner}/{repo} {clone_dir} && \\",
            f"cp -r {src}/. {target} && \\",
            f"rm -rf {clone_dir}",
            "```",
            "",
        ]
    parts.append("</details>")
    return "\n".join(parts)


def build_readme(owner, entries):
    rows = "\n".join(
        f"| [{repo}](https://github.com/{owner}/{repo}) | `{name}` | {desc} |"
        for repo, name, desc in entries
    )
    sections = "\n".join(
        f"### {name} — `{repo}`\n\n{desc}\n\n{deploy_block(owner, name, repo, skill_dir)}\n"
        for repo, name, skill_dir, desc in entries
    )
    return f"""# Agent Skills

> {owner} 的 Agent Skills 导航索引 · 跨 Claude Code / OpenCode / Codex 等 agentskills.io 兼容 harness。

本仓库由 [GitHub Actions](.github/workflows/update-skills.yml) 每日自动生成，收录清单见 [skills.yml](skills.yml)。

## 总览

| 仓库 | Skill | 说明 |
|---|---|---|
{rows}

## 详情与一键部署

{sections}
## 如何新增

在 [skills.yml](skills.yml) 的 `repos:` 列表追加一行目标仓库名并推送，Action 会自动重新生成本 README。
"""


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    owner, repos = load_config(root)
    if not repos:
        sys.exit("skills.yml 中没有可扫描的仓库")
    entries = []
    for repo in repos:
        try:
            meta = api_get(f"{API}/repos/{owner}/{repo}")
            branch = meta.get("default_branch", "main")
            dirs = scan_skill_dirs(owner, repo, branch)
            if not dirs:
                print(f"skip {repo}: no SKILL.md found")
                continue
            desc = readme_first_line(owner, repo, branch)
            if len(dirs) == 1:
                skill_dir = "" if dirs[0] == ROOT_MARKER else dirs[0]
                name = repo if skill_dir == "" else dirs[0]
            else:
                skill_dir, name = "", repo
            entries.append((repo, name, skill_dir, desc))
        except Exception as exc:
            print(f"skip {repo}: {exc}")
    if not entries:
        sys.exit("未发现任何 skill")
    readme = build_readme(owner, entries)
    target = os.path.join(root, "README.md")
    with open(target, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"generated {target} ({len(entries)} skills)")


if __name__ == "__main__":
    main()
