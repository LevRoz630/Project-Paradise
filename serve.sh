#!/usr/bin/env bash
# Quick local serve — works inside the devcontainer or any env with Ruby + Bundler.
# Usage: ./serve.sh

set -e

if ! command -v bundle &>/dev/null; then
  echo "Bundler not found. Install Ruby and run: gem install bundler"
  exit 1
fi

bundle check || bundle install
bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload
