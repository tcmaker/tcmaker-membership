class Signup::Progress < ApplicationRecord
  belongs_to :member

  scope :pending_activation, -> {
    where(account_creation_completed: true)
      .where(contact_record_creation_completed: true)
      .where(payment_info_completed: true)
      .where(liability_waiver_completed: true)
      .where(membership_activation_completed: false)
  }
end
