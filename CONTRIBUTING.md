# Contributing
You are more than welcome to submit issues and merge requests to this project.

# Git branches
Master branch is protected from pushes and may only accept fast-forwarded merge
from develop. Owners and masters are allowed to merge develop in master.

Develop branch  is protected from pushes.  It is the actual  working branch and
any kind of features  or bug fixes should be merged  to develop first.  Owners,
masters and developers are allowed to merge other branches to develop.  Masters
are allowed to push if and only if there is a real need (eg when develop branch
has to be rebased).

Anyone can  create a  new branch  for his own  needs. The  names of  the branch
should include the issue number if there is any issue related.

# Tests
Your commits must not break any tests.

# Commits format
Do your best to factor commits appropriately, ie not  too large  with
unrelated things in the same commit, and not too small  with the same small
change applied  N times in N different commits. If there was some accidental
reformatting or whitespace changes during the course of your  commits, please
rebase them away before submitting the MR.
