#!/usr/bin/env bash
set -euo pipefail

REPO=blackkcold/agent-skills
DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$DIR"

echo "==> 初始化仓库并创建 main 分支"
git init -b main

echo "==> 添加文件"
git add README.md LICENSE skills.yml .github

echo "==> 提交"
git -c user.name="blackkcold" -c user.email="blackkcold@users.noreply.github.com" commit -m "init: agent-skills 导航索引（README + Action 自动同步）"

echo "==> 添加远端（若尚未存在）"
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/${REPO}.git"

echo "==> 推送"
git push -u origin main

echo ""
echo "完成。Action 会在每日 02:00 及手动触发时自动重新生成 README。"
echo "访问 https://github.com/${REPO} 查看。"
