class AddFieldsToMembers < ActiveRecord::Migration[5.2]
  def change
    add_column :members, :stripe_identifier, :string
    add_column :members, :crm_identifier, :string
    add_column :members, :keyfob_code, :string
  end
end
