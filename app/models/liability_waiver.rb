class LiabilityWaiver
  include ActiveModel::Model

  attr_accessor :waives_liability

  validates :waives_liability, acceptance: true
end
