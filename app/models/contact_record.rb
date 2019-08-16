class ContactRecord < ApplicationRecord
  belongs_to :member

  validates :street_address, presence: true
  validates :city, presence: true
  validates :state_abbreviation, presence: true
  validates :postal_code, presence: true

  validates :phone, presence: true, phone: true

  validates :emergency_contact_name, presence: true
  validates :emergency_contact_phone, phone: true, presence: true

  def address_lines_to_display
    lines = [
      street_address,
      supplemental_address_1,
      supplemental_address_2,
      supplemental_address_3,
      "#{city}, #{state_abbreviation} #{postal_code}"
    ].select do |line|
      line =~ /\S/
    end
  end
end
