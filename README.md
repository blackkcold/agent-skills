# Agent Skills

> blackkcold 的 Agent Skills 导航索引 · 跨 Claude Code / OpenCode / Codex 等 agentskills.io 兼容 harness。

本仓库由 [GitHub Actions](.github/workflows/update-skills.yml) 每日自动生成，收录清单见 [skills.yml](skills.yml)。

## 总览

| 仓库 | Skill | 说明 |
|---|---|---|
| [sdd-skill](https://github.com/blackkcold/sdd-skill) | `sdd` | A compact, safety-gated workflow that turns unclear or risky coding requests into controlled, verifiable changes... |
| [release-skill](https://github.com/blackkcold/release-skill) | `release` | Automate your entire release workflow — version bump, CHANGELOG update, tag, build, and GitHub Release... |

## 详情与一键部署

### sdd — `sdd-skill`

A compact, safety-gated workflow that turns unclear or risky coding requests into controlled, verifiable changes...

<details>
<summary><b>sdd</b> · 一键部署</summary>

**通用 (任意 harness，下载到当前目录)**

```bash
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd ./sdd && rm -rf /tmp/sdd-skill-install
```

**OpenCode**

```bash
mkdir -p ~/.config/opencode/skills/sdd && \
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd/* ~/.config/opencode/skills/sdd/ && \
rm -rf /tmp/sdd-skill-install
```

**Claude Code**

```bash
mkdir -p ~/.claude/skills/sdd && \
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd/* ~/.claude/skills/sdd/ && \
rm -rf /tmp/sdd-skill-install
```

**Codex CLI**

```bash
mkdir -p ~/.codex/skills/sdd && \
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd/* ~/.codex/skills/sdd/ && \
rm -rf /tmp/sdd-skill-install
```

</details>

### release — `release-skill`

Automate your entire release workflow — version bump, CHANGELOG update, tag, build, and GitHub Release...

<details>
<summary><b>release</b> · 一键部署</summary>

**通用 (任意 harness，下载到当前目录)**

```bash
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release ./release && rm -rf /tmp/release-skill-install
```

**OpenCode**

```bash
mkdir -p ~/.config/opencode/skills/release && \
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release/* ~/.config/opencode/skills/release/ && \
rm -rf /tmp/release-skill-install
```

**Claude Code**

```bash
mkdir -p ~/.claude/skills/release && \
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release/* ~/.claude/skills/release/ && \
rm -rf /tmp/release-skill-install
```

**Codex CLI**

```bash
mkdir -p ~/.codex/skills/release && \
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release/* ~/.codex/skills/release/ && \
rm -rf /tmp/release-skill-install
```

</details>

## 如何新增

在 [skills.yml](skills.yml) 的 `repos:` 列表追加一行目标仓库名并推送，Action 会自动重新生成本 README。
