# Agent Skills

> blackkcold 的 Agent Skills 导航索引 · 跨 Claude Code / OpenCode / Codex 等 agentskills.io 兼容 harness。

本仓库由 [GitHub Actions](.github/workflows/update-skills.yml) 每日自动生成，收录清单见 [skills.yml](skills.yml)。

## 总览

| 仓库 | Skill | 说明 |
|---|---|---|
| [sdd-skill](https://github.com/blackkcold/sdd-skill) | `sdd` | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) |
| [release-skill](https://github.com/blackkcold/release-skill) | `release` | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) |
| [public-figure-research](https://github.com/blackkcold/public-figure-research) | `SKILL.md` | 通用公众人物调研 Skill —— 查询微博/抖音/小红书/B站四平台粉丝量，输出结构化 CSV 与标准报告，支持多领域（手机/3C、汽车、美妆等）。 |

## 详情与一键部署

### sdd — `sdd-skill`

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<details>
<summary><b>sdd</b> · 一键部署</summary>

**通用 (任意 harness，下载到当前目录)**

```bash
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd/. ./sdd && \
rm -rf /tmp/sdd-skill-install
```

**OpenCode**

```bash
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd/. ~/.config/opencode/skills/sdd && \
rm -rf /tmp/sdd-skill-install
```

**Claude Code**

```bash
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd/. ~/.claude/skills/sdd && \
rm -rf /tmp/sdd-skill-install
```

**Codex CLI**

```bash
git clone --depth 1 https://github.com/blackkcold/sdd-skill /tmp/sdd-skill-install && \
cp -r /tmp/sdd-skill-install/sdd/. ~/.codex/skills/sdd && \
rm -rf /tmp/sdd-skill-install
```

</details>

### release — `release-skill`

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<details>
<summary><b>release</b> · 一键部署</summary>

**通用 (任意 harness，下载到当前目录)**

```bash
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release/. ./release && \
rm -rf /tmp/release-skill-install
```

**OpenCode**

```bash
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release/. ~/.config/opencode/skills/release && \
rm -rf /tmp/release-skill-install
```

**Claude Code**

```bash
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release/. ~/.claude/skills/release && \
rm -rf /tmp/release-skill-install
```

**Codex CLI**

```bash
git clone --depth 1 https://github.com/blackkcold/release-skill /tmp/release-skill-install && \
cp -r /tmp/release-skill-install/release/. ~/.codex/skills/release && \
rm -rf /tmp/release-skill-install
```

</details>

### SKILL.md — `public-figure-research`

通用公众人物调研 Skill —— 查询微博/抖音/小红书/B站四平台粉丝量，输出结构化 CSV 与标准报告，支持多领域（手机/3C、汽车、美妆等）。

<details>
<summary><b>SKILL.md</b> · 一键部署</summary>

**通用 (任意 harness，下载到当前目录)**

```bash
git clone --depth 1 https://github.com/blackkcold/public-figure-research /tmp/public-figure-research-install && \
cp -r /tmp/public-figure-research-install/SKILL.md/. ./SKILL.md && \
rm -rf /tmp/public-figure-research-install
```

**OpenCode**

```bash
git clone --depth 1 https://github.com/blackkcold/public-figure-research /tmp/public-figure-research-install && \
cp -r /tmp/public-figure-research-install/SKILL.md/. ~/.config/opencode/skills/SKILL.md && \
rm -rf /tmp/public-figure-research-install
```

**Claude Code**

```bash
git clone --depth 1 https://github.com/blackkcold/public-figure-research /tmp/public-figure-research-install && \
cp -r /tmp/public-figure-research-install/SKILL.md/. ~/.claude/skills/SKILL.md && \
rm -rf /tmp/public-figure-research-install
```

**Codex CLI**

```bash
git clone --depth 1 https://github.com/blackkcold/public-figure-research /tmp/public-figure-research-install && \
cp -r /tmp/public-figure-research-install/SKILL.md/. ~/.codex/skills/SKILL.md && \
rm -rf /tmp/public-figure-research-install
```

</details>

## 如何新增

在 [skills.yml](skills.yml) 的 `repos:` 列表追加一行目标仓库名并推送，Action 会自动重新生成本 README。
