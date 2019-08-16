# frozen_string_literal: true

class Password
  include ActiveModel::Model
  attr_accessor :password

  PASSWORD_FORMAT = /\A
    (?=.{8,})          # Must contain 8 or more characters
    (?=.*\d)           # Must contain a digit
    (?=.*[a-z])        # Must contain a lower case character
    (?=.*[A-Z])        # Must contain an upper case character
    (?=.*[[:^alnum:]]) # Must contain a symbol
  /x.freeze

  validates :password,
            presence: true,
            confirmation: true,
            format: { with: PASSWORD_FORMAT, message: 'is not complex enough.' }

  validates :password_confirmation,
            presence: true
end
