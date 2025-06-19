# tst2

just tests

## 2025-06-19

I am using this repo to test stacked diffs with support of spr tool

- <https://spacedentist.github.io/spr/>

- the configuration for spr is set in `.git/config`

### simple

1. Pull main from upstream, and check it out.

2. Make your change, and run git commit. See this guide for what to put in your commit message.

3. Run spr diff. This will create a PR for your HEAD commit.

4. Wait for reviewers to approve. If you need to make changes:

    a. Make whatever changes you need in your working copy.

    b. Amend them into your HEAD commit with git commit --amend.

    c. Run spr diff. If you changed the commit message in the previous step, you will need to add the flag --update-message; see this guide for more detail.

    This will update the PR with the new version of your HEAD commit. spr will prompt you for a short message that describes what you changed. You can also pass the update message on the command line using the --message/-m flag of spr diff.

5. Once your PR is approved, run spr land to push it upstream.
