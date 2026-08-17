#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: ./install.sh [--target codex|claude|agents|gemini|openclaw|portable|custom|all] [--path DIR]

Installs the Gauntlet Loop Brain skill surface.
Use --target custom --path <agent-skill-root> for Hermes or another runtime
when its official skill root is known.
Set GAUNTLET_LOOP_BRAIN_INSTALL_HOME to test against a temporary home directory.
USAGE
}

target="codex"
custom_path=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --target) target="${2:?}"; shift 2 ;;
    --path) custom_path="${2:?}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

case "${target}" in codex|claude|agents|gemini|openclaw|portable|custom|all) ;; *) echo "ERROR: invalid target" >&2; exit 2 ;; esac
if [ "${target}" = "custom" ] && [ -z "${custom_path}" ]; then
  echo "ERROR: --target custom requires --path" >&2
  exit 2
fi

source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
base_home="${GAUNTLET_LOOP_BRAIN_INSTALL_HOME:-${HOME}}"
ownership_marker="gauntlet-loop-brain-owned:v1"

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

copy_tree() {
  local src="$1" dest="$2"
  mkdir -p "${dest}"
  (cd "${src}" && find . -type f ! -path '*/__pycache__/*' ! -name '*.pyc' -print0 | while IFS= read -r -d '' file; do
    mkdir -p "${dest}/$(dirname "${file}")"
    cp "${file}" "${dest}/${file}"
  done)
}

install_one() {
  local dest="$1"
  local parent base staging backup
  parent="$(dirname "${dest}")"
  base="$(basename "${dest}")"
  mkdir -p "${parent}"
  parent="$(cd "${parent}" && pwd -P)"
  dest="${parent}/${base}"
  staging="${parent}/.${base}.install.$$"
  backup="${parent}/.${base}.backup.$$"
  if [ -L "${dest}" ]; then
    echo "ERROR: refusing to replace symlink destination: ${dest}" >&2
    exit 1
  fi
  if [ -e "${dest}" ]; then
    if [ ! -d "${dest}" ] || [ ! -f "${dest}/.gauntlet-loop-brain-owned" ] || [ "$(cat "${dest}/.gauntlet-loop-brain-owned")" != "${ownership_marker}" ]; then
      echo "ERROR: refusing to replace unowned installation: ${dest}" >&2
      exit 1
    fi
    if ! python "${source_dir}/scripts/install_manifest.py" verify "${dest}"; then
      echo "ERROR: refusing to replace an installation with changed or user-added content: ${dest}" >&2
      exit 1
    fi
  fi
  if [ -e "${staging}" ] || [ -e "${backup}" ]; then
    echo "ERROR: installer staging path already exists for ${dest}" >&2
    exit 1
  fi
  mkdir -m 700 "${staging}"
  for file in SKILL.md AGENTS.md CLAUDE.md GEMINI.md README.md LICENSE CHANGELOG.md RELEASE_CHECKLIST.md PUBLISHING_NOTICE.md; do
    if [ -f "${source_dir}/${file}" ]; then
      cp "${source_dir}/${file}" "${staging}/${file}"
    fi
  done
  if [ -d "${source_dir}/agents" ]; then
    copy_tree "${source_dir}/agents" "${staging}/agents"
  fi
  copy_tree "${source_dir}/scripts" "${staging}/scripts"
  copy_tree "${source_dir}/assets/template-brain" "${staging}/assets/template-brain"
  copy_tree "${source_dir}/references" "${staging}/references"
  copy_tree "${source_dir}/docs" "${staging}/docs"
  printf '%s\n' "${ownership_marker}" > "${staging}/.gauntlet-loop-brain-owned"
  python "${source_dir}/scripts/install_manifest.py" create "${staging}"
  chmod -R go-rwx "${staging}"
  if [ -d "${dest}" ]; then
    mv "${dest}" "${backup}"
  fi
  if ! mv "${staging}" "${dest}"; then
    if [ -d "${backup}" ]; then mv "${backup}" "${dest}"; fi
    exit 1
  fi
  if [ -d "${backup}" ]; then rm -rf "${backup}"; fi
  echo "Gauntlet Loop Brain installed to ${dest}"
}

install_gemini() {
  local dest="${base_home}/.gemini/gauntlet-loop-brain"
  local loader="${base_home}/.gemini/GEMINI.md"
  mkdir -p "$(dirname "${loader}")"
  if [ -L "${loader}" ] || { [ -e "${loader}" ] && [ ! -f "${loader}" ]; }; then
    echo "ERROR: refusing non-regular or symlink Gemini loader: ${loader}" >&2
    exit 1
  fi
  install_one "${dest}"
  python "${source_dir}/scripts/gemini_loader.py" install "${loader}"
  echo "Gauntlet Loop Brain Gemini loader updated at ${loader}"
}

if [ "${target}" = "all" ]; then
  for name in codex claude agents openclaw portable; do
    install_one "$(target_dir "${name}")"
  done
  install_gemini
elif [ "${target}" = "gemini" ]; then
  install_gemini
else
  install_one "$(target_dir "${target}")"
fi
