#!/bin/bash
# =============================================================================
# sync-obsidian.sh — Auto-sync Obsidian vault antara VPS dan GitHub
# 
# Dipanggil oleh cron atau manual. Melakukan:
#   1. git pull (rebase)
#   2. git add semua perubahan lokal
#   3. git commit + push
#
# Vault path: /home/qwen-venice/obsidian-vault
# =============================================================================

set -euo pipefail

VAULT_PATH="/home/qwen-venice/obsidian-vault"
LOCK_FILE="${VAULT_PATH}/.sync.lock"
LOG_FILE="${VAULT_PATH}/logs/sync.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# Prevent concurrent runs
if [ -f "$LOCK_FILE" ]; then
    log "WARN: Sync already running (lock file exists). Exiting."
    exit 0
fi
trap "rm -f $LOCK_FILE" EXIT
touch "$LOCK_FILE"

cd "$VAULT_PATH"

# Ensure we have a remote
if ! git remote get-url origin &>/dev/null; then
    log "ERROR: No git remote 'origin' configured. Set it with:"
    log "  git remote add origin git@github.com:USER/REPO.git"
    exit 1
fi

log "=== Sync started ==="

# Pull latest from GitHub
log "Pulling from origin/main..."
if git pull origin main --rebase 2>&1 | tee -a "$LOG_FILE"; then
    log "Pull OK"
else
    log "WARN: Pull had conflicts or failed — continuing with local changes"
fi

# Stage all changes
git add .

# Only commit if there are changes
if git diff --cached --quiet; then
    log "No local changes to commit."
else
    COMMIT_MSG="Auto-sync: $(date -u '+%Y-%m-%d %H:%M UTC') — $(hostname)"
    git commit -m "$COMMIT_MSG" 2>&1 | tee -a "$LOG_FILE"
    log "Committed changes."

    # Push to GitHub
    if git push origin main 2>&1 | tee -a "$LOG_FILE"; then
        log "Push OK"
    else
        log "ERROR: Push failed — check network/auth"
        exit 1
    fi
fi

log "=== Sync complete ==="
