class AddPreferredPlanToSignupRecord < ActiveRecord::Migration[5.2]
  def change
    add_column(:signup_progresses, :preferred_plan, :string)
  end
end
