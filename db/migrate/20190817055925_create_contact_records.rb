class CreateContactRecords < ActiveRecord::Migration[5.2]
  def change
    create_table :contact_records do |t|
      t.references :member

      # Address
      t.string :street_address
      t.string :supplemental_address_1
      t.string :supplemental_address_2
      t.string :supplemental_address_3
      t.string :city
      t.string :state_abbreviation
      t.string :postal_code

      # Phone Number
      t.string :phone
      t.boolean :phone_can_receive_sms, null: false, default: false

      # Emergency Contact Information
      t.string :emergency_contact_name
      t.string :emergency_contact_phone

      t.timestamps
    end
  end
end
