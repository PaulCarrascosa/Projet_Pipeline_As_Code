# Git Workflow Guide

## Branch Strategy

### Main Branches

- **`main`** - Production-ready code
  - Protected branch
  - PR reviews required
  - Auto-deploys on merge
  - Tagged releases

- **`develop`** - Development branch
  - Integration branch
  - PRs from feature branches
  - Staging deployments

### Supporting Branches

#### Feature Branches
```bash
git checkout -b feature/feature-name develop

# Examples:
git checkout -b feature/add-book-search develop
git checkout -b feature/user-authentication develop
```

#### Bugfix Branches
```bash
git checkout -b bugfix/bug-name develop

# Examples:
git checkout -b bugfix/fix-loan-validation develop
```

#### Hotfix Branches
```bash
git checkout -b hotfix/hotfix-name main

# Examples:
git checkout -b hotfix/security-patch main
```

#### Release Branches
```bash
git checkout -b release/v1.0.0 develop
```

## Workflow: Adding a Feature

### 1. Create Feature Branch

```bash
# Update develop branch
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/user-authentication develop
```

### 2. Development Workflow

```bash
# Make changes and commit
git add .
git commit -m "feat: add JWT authentication"

# Commit message format:
# feat: add new feature
# fix: fix a bug
# docs: documentation updates
# style: code style changes
# refactor: code refactoring
# test: add/update tests
# chore: build/dependency updates
```

### 3. Keep Up With Develop

```bash
# Fetch latest changes
git fetch origin

# Rebase on develop (keeps history clean)
git rebase origin/develop

# Or merge if rebase conflicts are complex
git merge origin/develop
```

### 4. Push and Create PR

```bash
# Push feature branch
git push origin feature/user-authentication

# Create Pull Request on GitHub
# 1. Go to repository
# 2. Click "New Pull Request"
# 3. Select develop as target
# 4. Fill PR template
# 5. Request reviewers
```

### 5. Code Review & CI/CD

The CI/CD pipeline automatically:
- Runs linting and tests
- Analyzes code quality (SonarQube)
- Builds Docker image
- Comments on PR with results

### 6. Merge to Develop

Once approved:
```bash
# GitHub UI: Click "Squash and merge"
# Or command line:
git checkout develop
git pull origin develop
git merge --squash feature/user-authentication
git push origin develop

# Delete feature branch
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication
```

### 7. Release to Main

When ready for production:

```bash
# Create release PR from develop to main
# or via GitHub UI

# After merge to main, create tag:
git checkout main
git pull origin main
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## Commit Message Convention

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style
- `refactor`: Code refactoring
- `test`: Tests
- `chore`: Build/dependencies

### Examples

```bash
# Feature
git commit -m "feat(auth): add JWT token refresh endpoint"

# Bug fix
git commit -m "fix(books): correct pagination query"

# Documentation
git commit -m "docs(api): update endpoint documentation"

# Tests
git commit -m "test(users): add user creation tests"
```

## Handling Conflicts

### Merge Conflicts

```bash
# Start merge/rebase
git merge origin/develop
# Conflicts occur

# View conflicts
git status

# Edit conflicted files
# Look for markers: <<<<<<, ======, >>>>>>

# After fixing conflicts
git add .
git commit -m "merge: resolve conflicts from develop"
git push origin feature/branch-name
```

### Rebase Conflicts

```bash
# Start rebase
git rebase origin/develop
# Conflicts occur

# Fix files, then:
git add .
git rebase --continue

# To abort rebase
git rebase --abort
```

## Common Tasks

### Switch Branches

```bash
# List all branches
git branch -a

# Switch to existing branch
git checkout develop

# Create and switch to new branch
git checkout -b feature/new-feature develop
```

### View Commit History

```bash
# Simple log
git log --oneline

# Log with graph
git log --graph --oneline --all

# Log for specific branch
git log main..feature/branch-name
```

### Undo Changes

```bash
# Undo uncommitted changes (file)
git restore <file>

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Undo published commit (safe)
git revert <commit-hash>
```

### Stash Changes

```bash
# Stash uncommitted changes
git stash

# List stashed changes
git stash list

# Apply latest stash
git stash apply

# Apply specific stash
git stash apply stash@{n}

# Pop latest stash
git stash pop
```

## Syncing Fork with Upstream

If working with a fork:

```bash
# Add upstream remote
git remote add upstream <original-repo-url>

# Fetch upstream changes
git fetch upstream

# Rebase your main on upstream
git checkout main
git rebase upstream/main
git push origin main
```

## Best Practices

### ✅ Do

- Write clear commit messages
- Make atomic commits (one logical change)
- Rebase before pushing to keep history clean
- Test locally before pushing
- Review your own PR first
- Keep branches up to date with main/develop
- Use feature branches for all changes
- Squash commits when merging

### ❌ Don't

- Commit directly to `main` or `develop`
- Force push to shared branches
- Leave unrelated changes in one commit
- Ignore CI/CD failures
- Merge without code review
- Leave stale branches
- Commit sensitive data (.env, secrets)
- Rewrite public history

## GitHub Actions Integration

The `.github/workflows/ci-cd.yml` automatically:

1. Runs on push to `main` or `develop`
2. Runs on pull requests
3. Runs tests
4. Checks code quality
5. Builds Docker image
6. Pushes to Nexus (on main)

### View Workflow Status

```bash
# In GitHub UI: Actions tab
# On command line:
git log --graph --all
```

## Release Checklist

Before releasing to production:

- [ ] All tests passing
- [ ] Code review approved
- [ ] SonarQube quality gate passed
- [ ] CHANGELOG.md updated
- [ ] Version bumped (if using semver)
- [ ] Docker image built and tested
- [ ] Documentation updated
- [ ] Performance tested
- [ ] Security scan passed
- [ ] Deployment procedures reviewed

## Getting Help

```bash
# Git help
git help <command>
git help rebase
git help merge

# Show git config
git config --list

# Show remote URLs
git remote -v
```

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Commit Message Convention](https://www.conventionalcommits.org/)
- [Git Workflow Comparison](https://www.atlassian.com/git/tutorials/comparing-workflows)
