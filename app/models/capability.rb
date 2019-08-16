class Capability < ApplicationRecord
  has_many :endorsements
  has_many :members, through: :endorsements
end
