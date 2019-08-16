class CreateSignupProgresses < ActiveRecord::Migration[5.2]
  def change
    create_table :signup_progresses do |t|
      t.references :member
      t.boolean :account_creation_completed, null: false, default: false
      t.boolean :contact_record_creation_completed, null: false, default: false
      t.boolean :payment_info_completed, null: false, default: false
      t.boolean :liability_waiver_completed, null: false, default: false
      t.boolean :membership_activation_completed, null: false, default: false
      t.timestamps
    end
  end
end
