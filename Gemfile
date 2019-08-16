# frozen_string_literal: true

source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby '2.6.3'

gem 'pg', '>= 0.18', '< 2.0'
gem 'pry-rails'
gem 'puma', '~> 3.11'
gem 'rails', '~> 5.2.3'

gem 'bootstrap', '~> 4.3.1'
gem 'haml'
gem 'haml-rails'
gem 'jquery-rails'
gem 'sass-rails', '~> 5.0'
gem 'uglifier', '>= 1.3.0'

# AWS
gem 'aws-sdk'

# Auth
gem 'auth0', '4.8.0'
gem 'jwt'
gem 'cancancan'
gem 'openid_connect'

# Money stuff
gem 'stripe'

# Misc business logic
gem 'email_validator'
gem 'phonelib'

# Use ActiveStorage variant
# gem 'mini_magick', '~> 4.8'

# Reduces boot times through caching; required in config/boot.rb
# gem 'bootsnap', '>= 1.1.0', require: false

group :development, :test do
  gem 'dotenv-rails'
  gem 'rspec-rails', '~> 3.8'
  gem 'factory_bot_rails'
  gem 'shoulda-matchers'
  gem 'simplecov'
  gem 'faker'
  gem 'rubocop'
end

group :development do
  gem 'better_errors'
  gem 'binding_of_caller'

  gem 'listen', '>= 3.0.5', '< 3.2'
  gem 'spring'
  gem 'spring-watcher-listen', '~> 2.0.0'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: %i[mingw mswin x64_mingw jruby]
