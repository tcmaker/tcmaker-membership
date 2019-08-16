class Member < ApplicationRecord
  attr_accessor :password
  attr_accessor :password_confirmation

  has_one :contact_record
  has_one :pending_membership
  has_one :signup_progress, class_name: 'Signup::Progress'

  has_many :endorsements
  has_many :capabilities, through: :endorsements

  PASSWORD_FORMAT = /\A
    (?=.{8,})          # Must contain 8 or more characters
    (?=.*\d)           # Must contain a digit
    (?=.*[a-z])        # Must contain a lower case character
    (?=.*[A-Z])        # Must contain an upper case character
    (?=.*[[:^alnum:]]) # Must contain a symbol
  /x.freeze

  validates :first_name, presence: true
  validates :last_name, presence: true
  validates :email, email: true, uniqueness_on_idp: true
  validates :username, presence: true, uniqueness_on_idp: true
  validates :password,
    presence: true,
    confirmation: true,
    format: { with: PASSWORD_FORMAT, message: 'is not complex enough.' },
    on: :create
  # validates :password_confirmation, presence: true

  before_create :create_external_accounts
  after_update :update_external_accounts

  def name
    "#{first_name} #{last_name}"
  end

  protected

  def create_external_accounts
    Auth0Service.create_user!(self) # populates :sub
    ret = Stripe::Customer.create({
      email: self.email,
      name: self.name
    })
    self.stripe_identifier = ret.id
  end

  def update_external_accounts
    ret = Auth0Service.api_client.patch_user(self.sub, {
      given_name: self.first_name,
      family_name: self.last_name,
      name: "#{self.first_name} #{self.last_name}",
      email: self.email
    })
  end
end
