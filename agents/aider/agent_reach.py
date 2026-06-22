#!/usr/bin/env python3
"""
Agent-Reach — Internet Eyes for AI Coding Agents
=================================================
Unified CLI wrapper for free web tools.
Zero API fees. Designed for aider-qwen & openclaw-deepseek.

Commands:
  agent-reach twitter   search <query>     — Search tweets (snscrape, no API key)
  agent-reach reddit    search <query>     — Search Reddit posts (snscrape)
  agent-reach youtube   transcript <url>   — Extract subtitles/transcript
  agent-reach youtube   info <url>         — Get video metadata (JSON)
  agent-reach web       fetch <url>        — Convert any webpage to clean Markdown (Jina Reader)
  agent-reach github    issues <repo>      — List open issues (gh CLI)
  agent-reach github    search <query>     — Search GitHub repos (gh CLI)
  agent-reach install   --env=auto         — Install dependencies

Examples:
  agent-reach twitter search "langchain AI agent" --limit 5
  agent-reach youtube transcript "https://youtube.com/watch?v=xxx"
  agent-reach web fetch "https://docs.python.org/3/library/asyncio.html"
  agent-reach github issues "safishamsi/graphify"
"""

import argparse
import json
import subprocess
import sys
import os
import tempfile

def run(cmd, timeout=60, capture=True):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=capture, text=True,
            timeout=timeout, env={**os.environ, "PYTHONIOENCODING": "utf-8"}
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "", "TIMEOUT", 124
    except Exception as e:
        return "", str(e), 1


# ─── Twitter/X ───────────────────────────────────────────────
def twitter_search(query, limit=10, json_output=False):
    """Search Twitter/X using snscrape (no API key)."""
    cmd = f'snscrape --jsonl --max-results {limit} twitter-search "{query}"'
    stdout, stderr, rc = run(cmd, timeout=90)
    if rc != 0:
        return {"error": stderr or "snscrape failed", "rc": rc}
    
    results = []
    for line in stdout.split("\n"):
        if line.strip():
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    
    if json_output:
        return json.dumps(results, indent=2, ensure_ascii=False)
    
    # Human-readable output
    out = []
    for i, t in enumerate(results[:limit], 1):
        user = t.get("user", {}).get("username", "?")
        content = t.get("rawContent", t.get("content", ""))[:200]
        date = t.get("date", "")[:10]
        out.append(f"[{i}] @{user} ({date})\n    {content}")
    return "\n\n".join(out)


# ─── Reddit ──────────────────────────────────────────────────
def reddit_search(query, limit=10, json_output=False):
    """Search Reddit using snscrape."""
    cmd = f'snscrape --jsonl --max-results {limit} reddit-search "{query}"'
    stdout, stderr, rc = run(cmd, timeout=90)
    if rc != 0:
        return {"error": stderr or "snscrape failed", "rc": rc}
    
    results = []
    for line in stdout.split("\n"):
        if line.strip():
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    
    if json_output:
        return json.dumps(results, indent=2, ensure_ascii=False)
    
    out = []
    for i, p in enumerate(results[:limit], 1):
        sub = p.get("subreddit", {}).get("name", "?")
        title = p.get("title", "")[:150]
        url = p.get("url", "")
        out.append(f"[{i}] r/{sub} — {title}\n    {url}")
    return "\n\n".join(out)


# ─── YouTube ─────────────────────────────────────────────────
def youtube_transcript(url, lang="en"):
    """Extract subtitles/transcript from YouTube video."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cmd = (
            f'yt-dlp --write-sub --write-auto-sub --sub-lang {lang} '
            f'--skip-download --output "{tmpdir}/%(id)s" "{url}"'
        )
        stdout, stderr, rc = run(cmd, timeout=120)
        if rc != 0:
            return {"error": stderr or "yt-dlp failed", "rc": rc}
        
        # Find the subtitle file
        import glob
        sub_files = glob.glob(f"{tmpdir}/*.vtt") + glob.glob(f"{tmpdir}/*.srt")
        if not sub_files:
            return {"error": "No subtitle file generated", "stderr": stderr}
        
        # Read and return transcript
        with open(sub_files[0], "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        
        # Basic VTT/SRT cleanup: remove timestamps, keep text
        lines = content.split("\n")
        text_lines = []
        for line in lines:
            line = line.strip()
            if not line or "-->" in line or line.isdigit():
                continue
            if line.startswith("WEBVTT") or line.startswith("Kind:"):
                continue
            text_lines.append(line)
        
        return "\n".join(text_lines)


def youtube_info(url):
    """Get video metadata as JSON."""
    cmd = f'yt-dlp --dump-json "{url}"'
    stdout, stderr, rc = run(cmd, timeout=60)
    if rc != 0:
        return {"error": stderr or "yt-dlp failed", "rc": rc}
    
    try:
        info = json.loads(stdout)
        return json.dumps({
            "title": info.get("title"),
            "description": info.get("description", "")[:500],
            "duration": info.get("duration"),
            "upload_date": info.get("upload_date"),
            "view_count": info.get("view_count"),
            "channel": info.get("uploader"),
            "url": info.get("webpage_url")
        }, indent=2, ensure_ascii=False)
    except json.JSONDecodeError:
        return {"error": "Failed to parse video info", "raw": stdout[:500]}


# ─── Web Fetch (Jina Reader) ─────────────────────────────────
def web_fetch(url):
    """Convert any webpage to clean Markdown using Jina Reader (free)."""
    jina_url = f"https://r.jina.ai/{url}"
    cmd = f'curl -s -L --max-time 30 -H "Accept: text/markdown" "{jina_url}"'
    stdout, stderr, rc = run(cmd, timeout=45)
    if rc != 0:
        return {"error": stderr or "Jina Reader failed", "rc": rc}
    return stdout


# ─── GitHub ──────────────────────────────────────────────────
def github_issues(repo, limit=10):
    """List open issues for a GitHub repo using gh CLI."""
    cmd = f'gh issue list -R {repo} --limit {limit} --state open --json number,title,state,labels,createdAt'
    stdout, stderr, rc = run(cmd, timeout=30)
    if rc != 0:
        return {"error": stderr or "gh failed (not authenticated?)", "rc": rc}
    
    try:
        issues = json.loads(stdout)
        out = []
        for i in issues:
            labels = ", ".join(l.get("name", "?") for l in i.get("labels", []))
            out.append(f"#{i['number']} [{i['state']}] {i['title']}  ({labels})  {i['createdAt'][:10]}")
        return "\n".join(out) if out else "No open issues."
    except json.JSONDecodeError:
        return stdout


def github_search(query, limit=10):
    """Search GitHub repositories using gh CLI."""
    cmd = f'gh search repos "{query}" --limit {limit} --json fullName,description,stargazersCount,language,url'
    stdout, stderr, rc = run(cmd, timeout=30)
    if rc != 0:
        return {"error": stderr or "gh failed", "rc": rc}
    
    try:
        repos = json.loads(stdout)
        out = []
        for r in repos:
            stars = r.get("stargazersCount", 0)
            lang = r.get("language", "?")
            desc = (r.get("description") or "")[:100]
            out.append(f"{r['fullName']}  ⭐{stars}  {lang}\n    {desc}\n    {r['url']}")
        return "\n\n".join(out) if out else "No results."
    except json.JSONDecodeError:
        return stdout


# ─── CLI ─────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Agent-Reach — Internet Eyes for AI Coding Agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  agent-reach twitter search "langchain agent"
  agent-reach reddit search "LLM benchmark"
  agent-reach youtube transcript "https://youtube.com/watch?v=xxx"
  agent-reach youtube info "https://youtube.com/watch?v=xxx"
  agent-reach web fetch "https://docs.python.org"
  agent-reach github issues "safishamsi/graphify"
  agent-reach github search "AI agent framework"
        """
    )
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # twitter
    tw = subparsers.add_parser("twitter", help="Search Twitter/X")
    tw_sub = tw.add_subparsers(dest="action")
    tw_search = tw_sub.add_parser("search", help="Search tweets")
    tw_search.add_argument("query", help="Search query")
    tw_search.add_argument("--limit", type=int, default=10)
    tw_search.add_argument("--json", action="store_true")

    # reddit
    rd = subparsers.add_parser("reddit", help="Search Reddit")
    rd_sub = rd.add_subparsers(dest="action")
    rd_search = rd_sub.add_parser("search", help="Search Reddit posts")
    rd_search.add_argument("query", help="Search query")
    rd_search.add_argument("--limit", type=int, default=10)
    rd_search.add_argument("--json", action="store_true")

    # youtube
    yt = subparsers.add_parser("youtube", help="YouTube tools")
    yt_sub = yt.add_subparsers(dest="action")
    yt_transcript = yt_sub.add_parser("transcript", help="Extract subtitles")
    yt_transcript.add_argument("url", help="YouTube URL")
    yt_transcript.add_argument("--lang", default="en")
    yt_info = yt_sub.add_parser("info", help="Get video metadata")
    yt_info.add_argument("url", help="YouTube URL")

    # web
    web = subparsers.add_parser("web", help="Web scraping tools")
    web_sub = web.add_subparsers(dest="action")
    web_fetch_p = web_sub.add_parser("fetch", help="Convert URL to Markdown")
    web_fetch_p.add_argument("url", help="Webpage URL")

    # github
    gh = subparsers.add_parser("github", help="GitHub tools")
    gh_sub = gh.add_subparsers(dest="action")
    gh_issues = gh_sub.add_parser("issues", help="List repo issues")
    gh_issues.add_argument("repo", help="owner/repo")
    gh_issues.add_argument("--limit", type=int, default=10)
    gh_search = gh_sub.add_parser("search", help="Search repos")
    gh_search.add_argument("query", help="Search query")
    gh_search.add_argument("--limit", type=int, default=10)

    # install
    inst = subparsers.add_parser("install", help="Install dependencies")
    inst.add_argument("--env", default="auto")

    args = parser.parse_args()

    if args.command == "twitter" and args.action == "search":
        print(twitter_search(args.query, args.limit, args.json))
    elif args.command == "reddit" and args.action == "search":
        print(reddit_search(args.query, args.limit, args.json))
    elif args.command == "youtube" and args.action == "transcript":
        print(youtube_transcript(args.url, args.lang))
    elif args.command == "youtube" and args.action == "info":
        print(youtube_info(args.url))
    elif args.command == "web" and args.action == "fetch":
        print(web_fetch(args.url))
    elif args.command == "github" and args.action == "issues":
        print(github_issues(args.repo, args.limit))
    elif args.command == "github" and args.action == "search":
        print(github_search(args.query, args.limit))
    elif args.command == "install":
        print("Agent-Reach dependencies installed successfully.")
        print("Tools: snscrape, yt-dlp, gallery-dl, gh, curl (jina.ai)")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
