class CreateEndorsements < ActiveRecord::Migration[5.2]
  def change
    create_table :endorsements do |t|
      t.references :member
      t.references :capability
      t.bigint :granted_by_id
      t.timestamps
      t.index :granted_by_id, name: 'index_endorsements_on_granted_by_id'
    end
  end
end
