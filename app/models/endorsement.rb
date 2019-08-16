class Endorsement < ApplicationRecord
  belongs_to :member
  belongs_to :capability
end
