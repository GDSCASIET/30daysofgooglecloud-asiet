#!/bin/bash
git config --global user.name "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add -A
git commit -m "Update test.txt"
git push
