#!/usr/bin/env bash
set -euo pipefail

target="codex"
custom_path=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --target) target="${2:?}"; shift 2 ;;
    --path) custom_path="${2:?}"; shift 2 ;;
    -h|--help) echo "Usage: ./uninstall.sh [--target codex|claude|agents|gemini|openclaw|portable|custom|all] [--path DIR]"; exit 0 ;;
    *) echo "ERROR: unknown argument: $1" >&2; exit 2 ;;
  esac
done

case "${target}" in codex|claude|agents|gemini|openclaw|portable|custom|all) ;; *) echo "ERROR: invalid target" >&2; exit 2 ;; esac
if [ "${target}" = "custom" ] && [ -z "${custom_path}" ]; then
  echo "ERROR: --target custom requires --path" >&2
  exit 2
fi
base_home="${GAUNTLET_LOOP_BRAIN_INSTALL_HOME:-${HOME}}"
ownership_marker="gauntlet-loop-brain-owned:v1"
source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

target_dir() {
  case "$1" in
    codex) echo "${base_home}/.codex/skills/gauntlet-loop-brain" ;;
    claude) echo "${base_home}/.claude/skills/gauntlet-loop-brain" ;;
    agents) echo "${base_home}/.agents/skills/gauntlet-loop-brain" ;;
    openclaw) echo "${base_home}/.openclaw/skills/gauntlet-loop-brain" ;;
    portable) echo "${base_home}/.agent-skills/gauntlet-loop-brain" ;;
    custom) echo "${custom_path%/}/gauntlet-loop-brain" ;;
  esac
}

remove_one() {
  local dir="$1"
  if [ -L "${dir}" ]; then
    echo "ERROR: refusing to remove symlink destination: ${dir}" >&2
    return 1
  fi
  if [ -d "${dir}" ]; then
    if [ ! -f "${dir}/.gauntlet-loop-brain-owned" ] || [ "$(cat "${dir}/.gauntlet-loop-brain-owned")" != "${ownership_marker}" ]; then
      echo "ERROR: refusing to remove unowned installation: ${dir}" >&2
      return 1
    fi
    if ! python "${source_dir}/scripts/install_manifest.py" verify "${dir}"; then
      echo "ERROR: refusing to remove an installation with changed or user-added content: ${dir}" >&2
      return 1
    fi
    rm -rf "${dir}"
    echo "Removed ${dir}"
  else
    echo "Gauntlet Loop Brain is not installed at ${dir}"
  fi
}

remove_gemini() {
  local dir="${base_home}/.gemini/gauntlet-loop-brain"
  local loader="${base_home}/.gemini/GEMINI.md"
  if [ -L "${loader}" ] || { [ -e "${loader}" ] && [ ! -f "${loader}" ]; }; then
    echo "ERROR: refusing non-regular or symlink Gemini loader: ${loader}" >&2
    return 1
  fi
  remove_one "${dir}"
  if [ -f "${loader}" ]; then
    python "${source_dir}/scripts/gemini_loader.py" remove "${loader}"
    echo "Gauntlet Loop Brain Gemini loader cleaned at ${loader}"
  fi
}

if [ "${target}" = "all" ]; then
  for name in codex claude agents openclaw portable; do
    remove_one "$(target_dir "${name}")"
  done
  remove_gemini
elif [ "${target}" = "gemini" ]; then
  remove_gemini
else
  remove_one "$(target_dir "${target}")"
fi
