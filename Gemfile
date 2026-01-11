source "https://rubygems.org"

# Jekyll version compatible with GitHub Pages
gem "jekyll", "~> 4.3.0"

# Default theme
gem "minima", "~> 2.5"

# Jekyll plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
end

# Windows and JRuby does not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock http_parser.rb to 0.6.x on JRuby builds since newer versions may fail on JRuby
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# For link validation
gem "html-proofer", "~> 5.0", :group => :test
