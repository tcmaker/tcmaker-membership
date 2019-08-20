class CreateMemberships < ActiveRecord::Migration[5.2]
  def change
    create_table :memberships do |t|
      t.date :membership_started_at
      t.date :membership_expires_at
      t.string :stripe_subscription_identifier
      t.timestamps
    end
  end
end
