# Security

Do not open public issues containing credentials or private client data.

Report sensitive issues through the repository host's private vulnerability
reporting channel. The owner must enable that channel and replace this sentence
with the exact repository advisory URL before making the repository public. If
no private channel is available, do not publish sensitive details in an issue.

Private vulnerability reporting URL: OWNER_MUST_SET_AFTER_REPOSITORY_TARGET_EXISTS

Release gates scan for common API keys, private keys, OAuth tokens, local home
paths, and forbidden ZIP entries.

The installation inventory detects accidental or ordinary post-install drift.
It is not a trust root against a malicious process running as the same OS user.
Such a process can rewrite both installed content and its inventory. Environments
that include hostile same-user code need a separately protected verification
root, such as signed release metadata verified outside the installation tree,
filesystem isolation, or an appropriately trusted package manager.

Gemini loader edits use no-follow reads and same-directory atomic replacement.
Deterministic install and uninstall race tests prove that swapping the loader to
a symlink at the final mutation boundary does not modify the symlink target.

Security reports should include the affected version or commit, reproduction
steps, impact, and whether any secret or client data was exposed. Do not include
live credentials or private client artifacts.
