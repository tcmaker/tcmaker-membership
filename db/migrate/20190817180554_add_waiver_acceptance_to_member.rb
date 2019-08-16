class AddWaiverAcceptanceToMember < ActiveRecord::Migration[5.2]
  def change
    add_column :members, :accepted_liability_waiver, :boolean
  end
end
