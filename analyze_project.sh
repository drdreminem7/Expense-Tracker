#!/bin/bash

echo "Python files:"
find . -name "*.py"

echo ""
echo "Functions:"
grep -n "def " main.py

echo ""
echo "Git commits:"
git log --oneline
